import click
import subprocess
import platform
import os

# Function to set the background of your system
# Works on all operating systems.
# image_path: Absolute path to the image you want to set as the background
@click.command()
@click.argument('image_path', type=click.Path(exists=True))
def main(image_path):
    os_name = platform.system()

    try:
        # MacOS
        if os_name == 'Darwin':
            SCRIPT = ("/usr/bin/osascript<<END\n"
                    "tell application \"Finder\"\n"
                    "set desktop picture to POSIX file \"%s\"\n"
                    "end tell\n"
                    "END")
            
            subprocess.Popen(SCRIPT % image_path, shell=True)
            subprocess.call(["killall Dock"], shell=True)

        # Linux (Gnome)
        elif os_name == 'Linux':
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + image_path)

        # Window
        else:
            import ctypes
            SPI_SETDESKWALLPAPER = 20
            if isX64():
                ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
            else:
                ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 0)

        click.secho("Background Changed!", fg="green")

    except:
        click.secho("Could Not Change Background", fg="red")


def isX64():
    import struct
    return struct.calcsize('P') * 8 == 64


if __name__ == '__main__':
    main()
