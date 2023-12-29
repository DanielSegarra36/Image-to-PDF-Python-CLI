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


def biggest_dimension(images):
  widest = 0
  tallest = 0
  for img in images:
    currIMG = Image.open(f'{img}')
    if currIMG.size[0] > widest:
      widest = currIMG.size[0]
    if currIMG.size[1] > tallest:
      tallest = currIMG.size[1]
  return widest, tallest


def create_pdf(title, images):
  pdf_file = f"{title}.pdf"
  width, height = biggest_dimension(images)
  c = canvas.Canvas(pdf_file, pagesize=(width, height))

  for img in images:
    # black background
    c.setFillColorRGB(0, 0, 0)
    c.rect(0, 0, width, height, fill=True)

    # reset the x and y positions
    xPos = 0
    yPos = 0

    # if the image does not fit the page size, resize it
    currIMG = Image.open(f'{img}')
    if currIMG.size[0] > width or currIMG.size[1] > height:
      currIMG.thumbnail((width, height))
      currIMG.save(f'{img}', "JPEG")

    # center the image on the page
    xPos = (width - currIMG.size[0]) / 2
    yPos = (height - currIMG.size[1]) / 2

    # add the image to the PDF
    c.drawImage(img, xPos, yPos, width=currIMG.size[0], height=currIMG.size[1])
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

  try:
    images = fetch_images(urls)
    if images:
      create_pdf(title, images)
    else:
      print("No valid images found to create a PDF.")

  except requests.RequestException as e:
    print(f"Failed to fetch images: {e}")
  except Exception as e:
    print(f"An error occurred: {e}")
  finally:
    # Clean up: Remove the temporary folder and its contents
    if os.path.exists(".temp_images"):
      for file in os.listdir(".temp_images"):
        os.remove(os.path.join(".temp_images", file))
      os.rmdir(".temp_images")


if __name__ == "__main__":
  main()
