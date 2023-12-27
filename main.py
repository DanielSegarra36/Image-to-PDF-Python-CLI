import os
import argparse
import requests
from reportlab.pdfgen import canvas
from PIL import Image
from io import BytesIO
import urllib.parse

def extract_image_name(url):
    unquoted_url = urllib.parse.unquote(url)
    image_name = unquoted_url.split('/')[-1].split('&')[0]
    return image_name

def fetch_images(urls):
  images = []
  for url in urls:
    file_name = extract_image_name(url)
    response = requests.get(url)
    if response.status_code == 200:
      img = Image.open(BytesIO(response.content))
      if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

      # specify the new folder path
      new_folder_path = ".temp_images"

      # create the new folder if it does not exist
      os.makedirs(new_folder_path, exist_ok=True)

      # save the image in the new folder
      img.save(f"{new_folder_path}/{file_name}", "JPEG")
      images.append(f"{new_folder_path}/{file_name}")
    else:
      print(f"Failed to fetch image from {url}")
  return images


def create_pdf(title, images):
  pdf_file = f"{title}.pdf"
  rawIMG = Image.open(f'{images[0]}')
  c = canvas.Canvas(pdf_file, pagesize=(rawIMG.size[0], rawIMG.size[1]))

  for img in images:
    # print(f'image size: {rawIMG.size}')
    c.drawImage(img, 0, 0, width=rawIMG.size[0], height=rawIMG.size[1])
    c.showPage()
    # delete the image after it is added to the PDF
    os.remove(img)

  c.save()
  print(f"PDF {pdf_file} created successfully!")


def main():
  parser = argparse.ArgumentParser(
      description='Create a PDF with images from URLs')
  parser.add_argument('title', help='Title for the PDF')
  parser.add_argument('urls',
                      nargs='*',
                      help='URLs or path to a file containing URLs')

  args = parser.parse_args()
  title = args.title
  urls = args.urls

  if urls and urls[0].endswith(
      '.txt'):  # If a file containing URLs is provided
    with open(urls[0], 'r') as file:
      urls = file.read().splitlines()

  images = fetch_images(urls)
  create_pdf(title, images)


if __name__ == "__main__":
  main()
