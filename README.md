
<h1 align="center">SpotiNoAds</h1>

<p align="center">
  Una interfaz gráfica para parchear Spotify en Windows,<br/>
  sin escribir comandos en la terminal.
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
  <a href="https://github.com/hypeblock26/SpotiNoAds/releases/latest/download/SpotiNoAds.exe"><img src="https://img.shields.io/badge/Descargar-SpotiNoAds.exe-a6da95?colorA=363a4f&style=for-the-badge&logo=windows&logoColor=a6da95"></a>
</p>

<p align="center"> •
  <a href="#que-hace">Qué hace</a> •
  <a href="#requisitos">Requisitos</a> •
  <a href="#instalacion">Instalación</a> •
  <a href="#uso">Uso</a> •
  <a href="#presets">Presets</a> •
  <a href="#restaurar">Restaurar</a> •
  <a href="#faq">Preguntas frecuentes</a> •
  <a href="#aviso">Aviso</a>
</p>

<h1 id="que-hace">Qué hace</h1>

- **Bloquea anuncios** de banner, video y audio en el cliente de escritorio
- **Oculta podcasts, episodios y audiolibros** del inicio (opcional)
- **Bloquea las actualizaciones automáticas** de Spotify para que el parche no se pierda (opcional)
- **Reinstalación limpia** que borra Spotify por completo antes de instalarlo de nuevo
- **Botón de restaurar** que quita el parche y deja Spotify como estaba

<h1 id="requisitos">Requisitos</h1>

- **Sistema:** Windows 10 o 11
- **Internet:** el programa descarga Spotify y los archivos del parche al instalar
- **Spotify:** no hace falta tenerlo instalado, si no lo tienes el programa lo instala. La versión de Microsoft Store no sirve; el programa puede desinstalarla por ti

<h1 id="instalacion">Instalación</h1>

1. Dale al botón **Descargar** de arriba para bajar `SpotiNoAds.exe`. También puedes ir a [Releases](https://github.com/hypeblock26/SpotiNoAds/releases/latest).
2. Haz doble clic para abrirlo. No necesitas instalar nada más.

> **Windows SmartScreen:** como el programa no está firmado, puede salir "Windows protegió su PC". Dale a **Más información → Ejecutar de todos modos**.
>
> **Antivirus:** algunos pueden marcarlo como sospechoso porque modifica archivos de Spotify. Es un falso positivo.

<details>
<summary>Ejecutarlo desde el código</summary>

<br/>

Necesitas Python 3.8 o superior.

```
pip install customtkinter
python spotify_gui.py
```

</details>

<h1 id="uso">Uso</h1>

1. Cierra Spotify.
2. Abre SpotiNoAds.
3. Elige un preset o marca las opciones que quieras en las pestañas **Básico** y **Avanzado**.
4. Dale a **Instalar / Actualizar**, acepta el aviso y espera a que el log diga **Terminó correctamente**.

El bloqueo de anuncios siempre está activo, no tiene casilla. Las casillas son cambios extra: **Ocultar podcasts**, por ejemplo, los quita del inicio, y si no la marcas se quedan.

> Si quieres que se agreguen exclusiones a Microsoft Defender, abre el programa con clic derecho → **Ejecutar como administrador** y marca la opción en la pestaña **Avanzado**.

<h1 id="presets">Presets</h1>

| Preset | Qué hace |
|---|---|
| **Normal** | Tema nuevo |
| **Completa** | Tema nuevo, sin podcasts, sin secciones tipo anuncio, actualizaciones bloqueadas, abre Spotify al terminar y quita la versión de Microsoft Store si existe |
| **Premium** | Tema nuevo, sin bloquear anuncios (solo los de audio en podcasts). Para cuentas de pago |
| **Tema viejo** | Instala la versión 1.2.13 con el diseño anterior y bloquea las actualizaciones |

<h1 id="restaurar">Restaurar</h1>

El botón **Restaurar (quitar parche)** cierra Spotify y devuelve los archivos originales. No elimina las exclusiones de Defender ni los accesos directos.

Cierra Spotify del todo antes de usarlo, también desde la bandeja del sistema, junto al reloj. Si no, Windows no deja reemplazar los archivos.

<h1 id="faq">Preguntas frecuentes</h1>

**Spotify abre en negro o no carga después de instalar.**
Pasa cuando el parche no coincide con la versión que tenías. Abre SpotiNoAds, ve a **Avanzado**, marca **Reinstalación limpia** y vuelve a instalar. Esto borra Spotify por completo, incluidos sus ajustes y descargas sin conexión, así que tendrás que iniciar sesión otra vez.

**Los anuncios volvieron.**
Spotify se actualizó y borró el parche. Vuelve a instalar y marca **Bloquear actualizaciones** para que no se repita.

**Salen líneas que dicen `Didn't find variable ...` en el log.**
Son avisos. Algunos parches opcionales no encontraron dónde aplicarse en esa versión y el programa sigue con los demás.

**Quiero seguir viendo podcasts y audiolibros.**
No marques **Ocultar podcasts / episodios / audiolibros**. Si usas el preset **Completa**, desmárcala después de elegirlo.

<h1 id="aviso">Aviso</h1>

Este programa modifica archivos del cliente de Spotify (parchea binarios y quita firmas), así que úsalo bajo tu propio riesgo. Algunos antivirus pueden marcarlo como sospechoso por esto.

SpotiNoAds no está afiliado a Spotify AB ni cuenta con su respaldo. Spotify es una marca registrada de sus dueños.

<h1 id="licencia">Licencia</h1>

Consulta el archivo [LICENSE](LICENSE).
