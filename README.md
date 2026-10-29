<p align="center">
  <img src="https://github.com/user-attachments/assets/aeec0ac3-3e4e-47bd-a3d7-a8774de211b0" width="240" alt="Soundwave Emblem" />
</p>
<h1 align="center">SpotiNoAds</h1>

<p align="center">
  A graphical interface to patch Spotify on Windows,<br/>
  no terminal commands required.
</p>

<p align="center">
    <a href="https://github.com/hypeblock26/SpotiNoAds/stargazers"><img src="https://img.shields.io/github/stars/hypeblock26/SpotiNoAds?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
    <a href="https://github.com/hypeblock26/SpotiNoAds/forks"><img src="https://img.shields.io/github/forks/hypeblock26/SpotiNoAds?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
    <a href="https://github.com/hypeblock26/SpotiNoAds/issues"><img src="https://img.shields.io/github/issues/hypeblock26/SpotiNoAds?colorA=363a4f&colorB=ed8796&style=for-the-badge"></a>
    <a href="https://github.com/hypeblock26/SpotiNoAds/blob/main/LICENSE"><img src="https://img.shields.io/github/license/hypeblock26/SpotiNoAds?colorA=363a4f&colorB=f5bde6&style=for-the-badge&v=2"></a>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/python-3.8%2B-f5a97f?colorA=363a4f&style=for-the-badge&logo=python&logoColor=f5a97f">
    <img src="https://img.shields.io/badge/customtkinter-GUI-b7bdf8?colorA=363a4f&style=for-the-badge">
    <img src="https://img.shields.io/badge/powershell-5.1%2B-a6da95?colorA=363a4f&style=for-the-badge&logo=powershell&logoColor=a6da95">
</p>

<p align="center">
  <a href="https://github.com/hypeblock26/SpotiNoAds/releases/latest/download/SpotiNoAds.exe"><img src="https://img.shields.io/badge/Download-SpotiNoAds.exe-a6da95?colorA=363a4f&style=for-the-badge&logo=windows&logoColor=a6da95"></a>
</p>

<p align="center"> •
  <a href="#what-it-does">What it does</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#presets">Presets</a> •
  <a href="#restore">Restore</a> •
  <a href="#faq">FAQ</a> •
  <a href="#disclaimer">Disclaimer</a>
</p>

<h1 id="what-it-does">What it does</h1>

- **Blocks ads** (banner, video and audio) in the desktop client
- **Hides podcasts, episodes and audiobooks** from the home page (optional)
- **Blocks automatic Spotify updates** so the patch isn't lost (optional)
- **Clean reinstall** that completely removes Spotify before installing it again
- **Restore button** that removes the patch and leaves Spotify as it was

<h1 id="requirements">Requirements</h1>

- **System:** Windows 10 or 11
- **Internet:** the program downloads Spotify and the patch files during installation
- **Spotify:** you don't need to have it installed; if you don't, the program installs it. The Microsoft Store version doesn't work, but the program can uninstall it for you

<h1 id="installation">Installation</h1>

1. Click the **Download** button above to get `SpotiNoAds.exe`. You can also go to [Releases](https://github.com/hypeblock26/SpotiNoAds/releases/latest).
2. Double-click it to open it. You don't need to install anything else.

> **Windows SmartScreen:** since the program isn't signed, you may see "Windows protected your PC". Click **More info → Run anyway**.
>
> **Antivirus:** some may flag it as suspicious because it modifies Spotify files. This is a false positive.

<details>
<summary>Run it from source</summary>

<br/>

You need Python 3.8 or later.

```
pip install customtkinter
python spotify_gui.py
```

</details>

<h1 id="usage">Usage</h1>

1. Close Spotify.
2. Open SpotiNoAds.
3. Pick a preset, or check the options you want in the **Básico** (Basic) and **Avanzado** (Advanced) tabs.
4. Click **Instalar / Actualizar** (Install / Update), accept the prompt, and wait until the log says **Terminó correctamente** (Finished successfully).

Ad blocking is always on and has no checkbox. The checkboxes are extra changes: **Ocultar podcasts** (Hide podcasts), for example, removes them from the home page, and if you leave it unchecked they stay.

> If you want Microsoft Defender exclusions to be added, open the program with right-click → **Run as administrator** and check the option in the **Avanzado** tab.

<h1 id="presets">Presets</h1>

| Preset | What it does |
|---|---|
| **Normal** | New theme |
| **Completa** (Full) | New theme, no podcasts, no ad-like sections, updates blocked, opens Spotify when done, and removes the Microsoft Store version if present |
| **Premium** | New theme, ads not blocked (only the audio ads in podcasts). For paid accounts |
| **Tema viejo** (Old theme) | Installs version 1.2.13 with the previous design and blocks updates |

<h1 id="restore">Restore</h1>

The **Restaurar (quitar parche)** (Restore, remove patch) button closes Spotify and puts the original files back. It doesn't remove Defender exclusions or shortcuts.

Fully close Spotify before using it, including from the system tray next to the clock. Otherwise Windows won't let the files be replaced.

<h1 id="faq">FAQ</h1>

**Spotify opens black or doesn't load after installing.**
This happens when the patch doesn't match the version you had. Open SpotiNoAds, go to **Avanzado**, check **Reinstalación limpia** (Clean reinstall) and install again. This removes Spotify completely, including its settings and offline downloads, so you'll have to log in again.

**The ads came back.**
Spotify updated and wiped the patch. Install again and check **Bloquear actualizaciones** (Block updates) so it doesn't happen again.

**I see lines saying `Didn't find variable ...` in the log.**
These are warnings. Some optional patches couldn't find where to apply in that version, and the program continues with the rest.

**I want to keep seeing podcasts and audiobooks.**
Don't check **Ocultar podcasts / episodios / audiolibros** (Hide podcasts / episodes / audiobooks). If you use the **Completa** preset, uncheck it after selecting the preset.

<h1 id="disclaimer">Disclaimer</h1>

This program modifies files of the Spotify client (it patches binaries and removes signatures), so use it at your own risk. Some antivirus programs may flag it as suspicious because of this.

SpotiNoAds is not affiliated with or endorsed by Spotify AB. Spotify is a registered trademark of its respective owners.

<h1 id="license">License</h1>

See the [LICENSE](LICENSE) file.
