import argparse
import urllib.request
import re

def liste_les_images(url: str) -> []:
    domain = url.split('/')[2]
    u = urllib.request.urlopen(url)
    images_urls = []
    try:
        data = u.read().decode('utf-8')
        print(data)
    finally:
        u.close()

    img_re = re.compile('<a href="/assets.*">')
    imgs = img_re.findall(data)

    for img in imgs:
        parse=img.split('"')[1]
        url_img = "https://" + domain + parse
        images_urls.append(url_img)

    return images_urls

def telecharge(image: str):
    image_name = image.split('/')[-1]
    with urllib.request.urlopen(image) as resp:
        data = resp.read()
        with open(image_name, 'wb') as file:
            file.write(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Télécharge toutes les images d'une url")
    parser.add_argument("url", type=str, help="url")
    args = parser.parse_args()

    images = liste_les_images(args.url)
    for image in images:
        telecharge(image)
