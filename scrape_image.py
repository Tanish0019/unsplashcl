import click
import requests
from bs4 import BeautifulSoup

# Function to download the image of the day from https://unsplash.com
@click.command()
def main():
    url = 'https://unsplash.com/'
    try:
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        img = soup.find('picture').find('img')
        img_url = img['src']
        img_data = requests.get(img_url).content
        with open('image_of_the_day.jpg', 'wb') as f:
            f.write(img_data)
        click.secho('Successfully Downloaded Image', fg='green')

    except:
        click.secho("Could not get image", fg='red')

if __name__ == "__main__":
    main()
