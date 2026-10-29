import ctypes
import os
import queue
import re
import subprocess
import sys
import threading
from pathlib import Path

import customtkinter as ctk
from tkinter import messagebox

APP_DIR = Path(sys.executable).parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parent
OLD_THEME_VERSION = "1.2.13.661.ga588f749"
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)

LYRICS_THEMES = [
    "(ninguno)", "blue", "blueberry", "discord", "drot", "default", "forest", "fresh",
    "github", "lavender", "orange", "postlight", "pumpkin", "purple", "radium", "relish",
    "red", "sandbar", "spotify", "spotify#2", "strawberry", "turquoise", "yellow",
    "zing", "pinkle", "krux", "royal", "oceano",
]

BASIC = [
    ("new_theme", "-new_theme", "Tema nuevo (barras laterales nuevas)"),
    ("podcasts_off", None, "Ocultar podcasts / episodios / audiolibros"),
    ("block_update", None, "Bloquear actualizaciones automáticas de Spotify"),
    ("adsections_off", "-adsections_off", "Ocultar secciones tipo anuncio"),
    ("premium", "-premium", "Modo Premium (no bloquea ads, solo audio ads en podcasts)"),
    ("start_spoti", "-start_spoti", "Abrir Spotify al terminar"),
    ("no_shortcut", "-no_shortcut", "No crear acceso directo en el escritorio"),
    ("DisableStartup", "-DisableStartup", "Que Spotify no arranque con Windows"),
]

ADVANCED = [
    ("canvashome_off", "-canvashome_off", "Quitar canvas del home"),
    ("lyrics_block", "-lyrics_block", "Desactivar letras nativas"),
    ("sendversion_off", "-sendversion_off", "No enviar info de versión"),
    ("topsearchbar", "-topsearchbar", "Barra de búsqueda arriba"),
    ("newFullscreenMode", "-newFullscreenMode", "Modo pantalla completa nuevo (experimental)"),
    ("homesub_off", "-homesub_off", "Quitar chips de filtro del home"),
    ("hide_col_icon_off", "-hide_col_icon_off", "NO ocultar ícono de colaboradores"),
    ("rightsidebar_off", "-rightsidebar_off", "Desactivar barra derecha nueva"),
    ("rightsidebarcolor", "-rightsidebarcolor", "Barra derecha con color de la portada"),
    ("plus", "-plus", "Mantener botón Plus en vez del corazón"),
    ("funnyprogressBar", "-funnyprogressBar", "Barra de progreso rara"),
    ("exp_spotify", "-exp_spotify", "Solo experimentos de Spotify"),
    ("devtools", "-devtools", "Modo desarrollador"),
    ("mirror", "-m", "Usar mirror (si GitHub raw falla)"),
    ("confirm_uninstall_ms_spoti", "-confirm_uninstall_ms_spoti",
     "Desinstalar Spotify de Microsoft Store si existe"),
]

PRESETS = {
    "Normal": {"new_theme": True},
    "Completa": {
        "new_theme": True, "podcasts_off": True, "block_update": True,
        "adsections_off": True, "start_spoti": True,
        "confirm_uninstall_ms_spoti": True, "lyrics": "spotify",
    },
    "Premium": {"premium": True, "new_theme": True},
    "Tema viejo": {"version": OLD_THEME_VERSION, "block_update": True},
}

NOISE = re.compile(r"^[#=\-\s\d.,%]*$")


def is_admin():
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except Exception:
        return False


def oem_encoding():
    try:
        "".encode("oem")
        return "oem"
    except LookupError:
        return "cp850"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SpotiNoAds")
        self.geometry("760x780")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.vars = {}
        self.q = queue.Queue()
        self.proc = None
        self.busy = False

        self._build()
        self._apply_preset("Normal")
        self.after(100, self._drain)

    def _build(self):
        ctk.CTkLabel(self, text="SpotiNoAds", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=(12, 0))

        pf = ctk.CTkFrame(self)
        pf.pack(fill="x", padx=14, pady=10)
        ctk.CTkLabel(pf, text="Preset:").pack(side="left", padx=(10, 6))
        for name in PRESETS:
            ctk.CTkButton(pf, text=name, width=90,
                          command=lambda n=name: self._apply_preset(n)).pack(side="left", padx=4, pady=8)

        tabs = ctk.CTkTabview(self, height=330)
        tabs.pack(fill="x", padx=14)
        t1, t2 = tabs.add("Básico"), tabs.add("Avanzado")

        for key, _, text in BASIC:
            self.vars[key] = ctk.BooleanVar()
            ctk.CTkCheckBox(t1, text=text, variable=self.vars[key]).pack(anchor="w", padx=10, pady=4)

        sf = ctk.CTkScrollableFrame(t2)
        sf.pack(fill="both", expand=True)
        for key, _, text in ADVANCED:
            self.vars[key] = ctk.BooleanVar()
            ctk.CTkCheckBox(sf, text=text, variable=self.vars[key]).pack(anchor="w", padx=6, pady=3)

        self.vars["defender"] = ctk.BooleanVar()
        ctk.CTkCheckBox(sf, text="Agregar exclusiones a Defender (requiere abrir como administrador)",
                        variable=self.vars["defender"]).pack(anchor="w", padx=6, pady=3)

        row = ctk.CTkFrame(sf, fg_color="transparent")
        row.pack(fill="x", pady=(10, 2))
        ctk.CTkLabel(row, text="Versión de Spotify (vacío = recomendada):").pack(side="left", padx=6)
        self.vars["version"] = ctk.StringVar()
        ctk.CTkEntry(row, textvariable=self.vars["version"], width=190,
                     placeholder_text="ej. 1.2.88").pack(side="left")

        row = ctk.CTkFrame(sf, fg_color="transparent")
        row.pack(fill="x", pady=2)
        ctk.CTkLabel(row, text="Tema de letras:").pack(side="left", padx=6)
        self.vars["lyrics"] = ctk.StringVar(value=LYRICS_THEMES[0])
        ctk.CTkOptionMenu(row, values=LYRICS_THEMES, variable=self.vars["lyrics"], width=160).pack(side="left")

        row = ctk.CTkFrame(sf, fg_color="transparent")
        row.pack(fill="x", pady=2)
        ctk.CTkLabel(row, text="Límite de caché de audio (MB, 500-20000):").pack(side="left", padx=6)
        self.vars["cache_limit"] = ctk.StringVar()
        ctk.CTkEntry(row, textvariable=self.vars["cache_limit"], width=90).pack(side="left")

        row = ctk.CTkFrame(sf, fg_color="transparent")
        row.pack(fill="x", pady=2)
        ctk.CTkLabel(row, text="Si ya hay otra versión instalada:").pack(side="left", padx=6)
        self.vars["existing"] = ctk.StringVar(value="Instalar encima")
        ctk.CTkOptionMenu(row, values=["Instalar encima", "Desinstalar y reinstalar"],
                          variable=self.vars["existing"], width=190).pack(side="left")

        bf = ctk.CTkFrame(self, fg_color="transparent")
        bf.pack(fill="x", padx=14, pady=10)
        self.btn_install = ctk.CTkButton(bf, text="Instalar / Actualizar", height=38, command=self.on_install)
        self.btn_install.pack(side="left", expand=True, fill="x", padx=(0, 6))
        self.btn_restore = ctk.CTkButton(bf, text="Restaurar (quitar parche)", height=38,
                                         fg_color="#8a3b3b", hover_color="#6e2e2e", command=self.on_restore)
        self.btn_restore.pack(side="left", expand=True, fill="x", padx=(6, 0))

        self.log = ctk.CTkTextbox(self, font=ctk.CTkFont(family="Consolas", size=12))
        self.log.pack(fill="both", expand=True, padx=14, pady=(0, 12))
        self.log.configure(state="disabled")
        self._log("Listo. Elige un preset u opciones y dale a Instalar.")
        if not is_admin():
            self._log("Nota: no estás como administrador. Las exclusiones de Defender se omitirán.")

    def _apply_preset(self, name):
        p = PRESETS[name]
        for key, v in self.vars.items():
            if isinstance(v, ctk.BooleanVar):
                v.set(bool(p.get(key, False)))
        self.vars["version"].set(p.get("version", ""))
        self.vars["lyrics"].set(p.get("lyrics", LYRICS_THEMES[0]))
        self.vars["existing"].set("Instalar encima")

    def _log(self, text):
        self.q.put(text)

    def _drain(self):
        try:
            while True:
                line = self.q.get_nowait()
                self.log.configure(state="normal")
                self.log.insert("end", line.rstrip("\n") + "\n")
                self.log.see("end")
                self.log.configure(state="disabled")
        except queue.Empty:
            pass
        self.after(100, self._drain)

    def _set_busy(self, busy):
        self.busy = busy
        st = "disabled" if busy else "normal"
        self.btn_install.configure(state=st)
        self.btn_restore.configure(state=st)

    def build_flags(self):
        g = lambda k: self.vars[k].get()
        flags = ["-no_pause"]
        flags.append("-podcasts_off" if g("podcasts_off") else "-podcasts_on")
        flags.append("-block_update_on" if g("block_update") else "-block_update_off")

        for key, flag, _ in BASIC + ADVANCED:
            if flag and g(key):
                flags.append(flag)

        if not (g("defender") and is_admin()):
            flags.append("-defender_exclusions_off")

        if g("existing") == "Desinstalar y reinstalar":
            flags.append("-confirm_spoti_recomended_uninstall")
        else:
            flags.append("-confirm_spoti_recomended_over")

        ver = g("version").strip()
        if ver:
            flags += ["-v", ver]
        ly = g("lyrics")
        if ly and ly != LYRICS_THEMES[0]:
            flags += ["-lyrics_stat", ly]
        cl = g("cache_limit").strip()
        if cl.isdigit():
            flags += ["-cache_limit", cl]
        return flags

    def on_install(self):
        if self.busy:
            return
        ver = self.vars["version"].get().strip()
        if ver and not re.match(r"^\d+\.\d+\.\d+(\.\d+(\.g[0-9a-f]+)?)?$", ver):
            messagebox.showerror("Versión inválida", "Formato esperado: 1.2.88 o 1.2.88.485.g1012a6e0")
            return
        if not messagebox.askokcancel(
            "Confirmar",
            "Esto modifica archivos de Spotify (parchea binarios, quita firmas y puede\n"
            "agregar exclusiones en Defender). Úsalo bajo tu propio riesgo.\n\n¿Continuar?",
        ):
            return
        if self.vars["defender"].get() and not is_admin():
            self._log("Aviso: sin permisos de administrador no se agregan exclusiones a Defender.")
        self._set_busy(True)
        threading.Thread(target=self._install_worker, daemon=True).start()

    def _install_worker(self):
        try:
            script = APP_DIR / "run.ps1"
            if not script.exists():
                raise RuntimeError(f"No encuentro run.ps1 en {APP_DIR}")

            flags = self.build_flags()
            self._log("Flags: " + " ".join(flags))
            cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
                   "-File", str(script)] + flags
            self.proc = subprocess.Popen(
                cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, encoding=oem_encoding(), errors="replace", creationflags=NO_WINDOW,
            )
            for line in self.proc.stdout:
                line = line.strip("\r\n")
                if line.strip() and not NOISE.match(line):
                    self._log(line)
            code = self.proc.wait()
            self._log("Terminó correctamente." if code == 0 else f"Terminó con código {code}.")
        except Exception as e:
            self._log(f"ERROR: {e}")
        finally:
            self.proc = None
            self.after(0, lambda: self._set_busy(False))

    def on_restore(self):
        if self.busy:
            return
        if not messagebox.askokcancel("Restaurar", "Se cerrará Spotify y se restaurarán los archivos originales.\n¿Seguir?"):
            return
        self._set_busy(True)
        threading.Thread(target=self._restore_worker, daemon=True).start()

    def _restore_worker(self):
        try:
            sp = Path(os.environ["APPDATA"]) / "Spotify"
            pairs = [
                (sp / "chrome_elf.dll.bak", sp / "chrome_elf.dll"),
                (sp / "Spotify.dll.bak", sp / "Spotify.dll"),
                (sp / "Spotify.bak", sp / "Spotify.exe"),
                (sp / "Apps" / "xpui.bak", sp / "Apps" / "xpui.spa"),
            ]
            found = [(b, t) for b, t in pairs if b.exists()]
            if not found:
                self._log("No encontré respaldos: Spotify no tiene el parche (o ya se quitó).")
                return
            subprocess.run(["taskkill", "/F", "/IM", "Spotify.exe"],
                           capture_output=True, creationflags=NO_WINDOW)
            for bak, target in found:
                try:
                    os.replace(bak, target)
                    self._log(f"Restaurado: {target.name}")
                except OSError as e:
                    self._log(f"ERROR restaurando {target.name}: {e}")
                    return
            self._log("Parche removido. (Las exclusiones de Defender y los accesos directos no se tocan.)")
        except Exception as e:
            self._log(f"ERROR: {e}")
        finally:
            self.after(0, lambda: self._set_busy(False))


if __name__ == "__main__":
    if sys.platform != "win32":
        print("Esto solo funciona en Windows.")
    App().mainloop()