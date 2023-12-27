# PDF Creator from Images

This project is a simple Python script that creates a PDF from a list of images.

## Features

- Creates a PDF with the dimensions of the actual images
- Deletes the images after they are added to the PDF

## Usage

The script takes a title for the PDF as a command-line argument.

```bash
python main.py <NEW_PDF_NAME> <URL_PER_LINE_FILE.txt>
```

or using `poetry`

```
poetry run python main.py <NEW_PDF_NAME> <URL_PER_LINE_FILE.txt>
```

## Dependencies

- Python 3
- reportlab
- PIL

## Installation

1. Clone this repository
2. Install the dependencies

```
pip install reportlab pillow
```

3. Run the script with a title for the PDF as a command-line argument

```
python main.py  <NEW_PDF_NAME> <URL_PER_LINE_FILE.txt>
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
[MIT](https://choosealicense.com/licenses/mit/)
