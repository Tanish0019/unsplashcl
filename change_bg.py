import click
import subprocess
import platform
import os

@click.command()
@click.argument('image_path', type=click.Path(exists=True))
def main(image_path):
    os_name = platform.system()
    if os_name == 'Darwin':
        SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""
        subprocess.Popen(SCRIPT % image_path, shell=True)
        subprocess.call(["killall Dock"], shell=True)

    elif os_name == 'Linux':
        pass
    
    else:
        pass
    

if __name__ == '__main__':
    main()
