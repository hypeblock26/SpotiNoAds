<h1 align="center">SpotiNoAds</h1>

<p align="center">
  Una interfaz gráfica para parchear Spotify en Windows,<br/>
  sin escribir comandos en la terminal.
</p>

<p align="center">
    <a href="https://github.com/HYPEBLOCK26/SpotiNoAds/stargazers"><img src="https://img.shields.io/github/stars/HYPEBLOCK26/SpotiNoAds?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
    <a href="https://github.com/HYPEBLOCK26/SpotiNoAds/forks"><img src="https://img.shields.io/github/forks/HYPEBLOCK26/SpotiNoAds?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
    <a href="https://github.com/HYPEBLOCK26/SpotiNoAds/issues"><img src="https://img.shields.io/github/issues/HYPEBLOCK26/SpotiNoAds?colorA=363a4f&colorB=ed8796&style=for-the-badge"></a>
    <a href="https://github.com/HYPEBLOCK26/SpotiNoAds/blob/main/LICENSE"><img src="https://img.shields.io/github/license/HYPEBLOCK26/SpotiNoAds?colorA=363a4f&colorB=f5bde6&style=for-the-badge&v=2"></a>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/python-3.8%2B-f5a97f?colorA=363a4f&style=for-the-badge&logo=python&logoColor=f5a97f">
    <img src="https://img.shields.io/badge/customtkinter-GUI-b7bdf8?colorA=363a4f&style=for-the-badge">
    <img src="https://img.shields.io/badge/powershell-5.1%2B-a6da95?colorA=363a4f&style=for-the-badge&logo=powershell&logoColor=a6da95">
</p>

<p align="center"> •
  <a href="#requisitos">Requisitos</a> •
  <a href="#que-hace">Qué hace</a> •
  <a href="#instalacion">Instalación</a> •
  <a href="#presets">Presets</a> •
  <a href="#restaurar">Restaurar</a> •
  <a href="#aviso">Aviso</a>
</p>

<h1 id="requisitos">Requisitos</h1>

- **Sistema:** Windows 10 o 11
- **Spotify:** versión de escritorio instalada desde la página oficial (la de Microsoft Store no sirve)
- **PowerShell:** 5.1 o superior
- **Python:** 3.8 o superior, solo si vas a correrlo desde el código

<h1 id="que-hace">Qué hace</h1>

- **Bloquea anuncios** de banner, video y audio en el cliente de escritorio
- **Oculta podcasts, episodios y audiolibros** del inicio (opcional)
- **Bloquea las actualizaciones automáticas** de Spotify (opcional)
- **Presets listos** para instalar con un clic, y una pestaña avanzada para ajustar cada opción
- **Preguntas en ventanas** de Sí/No, en vez de escribir `Y` o `N` en la consola
- **Botón de restaurar** que deja Spotify como estaba

<h1 id="instalacion">Instalación</h1>

1. Instala las dependencias:

```
pip install customtkinter
```

2. Abre la interfaz:

```
python spotify_gui.py
```

3. Elige un preset o marca las opciones que quieras y dale a **Instalar / Actualizar**.

> Si quieres que se agreguen exclusiones a Microsoft Defender, abre la interfaz como administrador y marca la opción en la pestaña **Avanzado**.

<h1 id="presets">Presets</h1>

| Preset | Qué hace |
|---|---|
| **Normal** | Tema nuevo |
| **Completa** | Tema nuevo, sin podcasts, sin secciones tipo anuncio, actualizaciones bloqueadas, abre Spotify al terminar y quita la versión de Microsoft Store si existe |
| **Premium** | Tema nuevo, sin bloquear anuncios (solo los de audio en podcasts). Para cuentas de pago |
| **Tema viejo** | Instala la versión 1.2.13 con el diseño anterior y bloquea las actualizaciones |

<h1 id="restaurar">Restaurar</h1>

El botón **Restaurar (quitar parche)** cierra Spotify y devuelve los archivos originales. No elimina las exclusiones de Defender ni los accesos directos.

<h1 id="aviso">Aviso</h1>

Este programa modifica archivos del cliente de Spotify (parchea binarios y quita firmas), así que úsalo bajo tu propio riesgo. Algunos antivirus pueden marcarlo como sospechoso por esto.

SpotiNoAds no está afiliado a Spotify AB ni cuenta con su respaldo. Spotify es una marca registrada de sus dueños.

<h1 id="licencia">Licencia</h1>

Consulta el archivo [LICENSE](LICENSE).