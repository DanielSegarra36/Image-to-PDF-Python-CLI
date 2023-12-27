import argparse
import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
from io import BytesIO

def fetch_images(urls):
    images = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            images.append(img)
        else:
            print(f"Failed to fetch image from {url}")
    return images

def create_pdf(title, images):
    pdf_file = f"{title}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    for img in images:
        c.drawImage(img, 0, 0, width=letter[0], height=letter[1])
        c.showPage()

    c.save()
    print(f"PDF {pdf_file} created successfully!")

def main():
    parser = argparse.ArgumentParser(description='Create a PDF with images from URLs')
    parser.add_argument('title', help='Title for the PDF')
    parser.add_argument('urls', nargs='*', help='URLs or path to a file containing URLs')

    args = parser.parse_args()
    title = args.title
    urls = args.urls

    if urls and urls[0].endswith('.txt'):  # If a file containing URLs is provided
        with open(urls[0], 'r') as file:
            urls = file.read().splitlines()

    images = fetch_images(urls)
    create_pdf(title, images)

if __name__ == "__main__":
    main()