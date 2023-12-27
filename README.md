# PDF Creator from Images

This project is a simple Python script that creates a PDF from a list of images.

## Features

- Creates a PDF with the dimensions of the actual images
- Deletes the images after they are added to the PDF

## Usage

The script takes a title for the PDF as a command-line argument.

```
python main.py <NEW_PDF_NAME> [URL_1 URL_2 ...] | [<URL_PER_LINE_FILE.txt>]
```

or using `poetry`

```
poetry run python main.py <NEW_PDF_NAME> [URL_1 URL_2 ...] | [<URL_PER_LINE_FILE.txt>]
```

### Arguments

1. File Name

- `<NEW_PDF_NAME>`  
  can be replaced with the name of the PDF file to be created. _(does **NOT** need to include extension, **i.e. '.pdf'**)_

2. One or more space-separated URLs

- `URL_1 URL_2 ... `  
  can be replaced with a list of URLs separated by spaces.

  or a file with one URL per line.

- `<URL_PER_LINE_FILE.txt>` can be replaced with a list of URLs separated by spaces or a file with one URL per line.

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

3.

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repository
   ```
   git clone https://github.com/DanielSegarra36/Image-to-PDF-Python-CLI.git
   ```

#### Manual

2. Use a virtual environment _(optional)_
   ```
   python3 -m venv .venv
   . .venv/bin/activate
   ```
3. Install the dependencies using requirements.txt:
   ```
   pip install -r requirements.txt
   ```
4. Run the script with a title for the PDF as a command-line argument
   ```
   python main.py <NEW_PDF_NAME> [URL_1 URL_2 ...] | [<URL_PER_LINE_FILE.txt>]
   ```

#### Using pipx & poetry _(recommended)_

[pipx](https://github.com/pypa/pipx#on-macos) is used to install Python CLI applications globally while still **_isolating them in virtual environments_**.

[Poetry](https://python-poetry.org/docs/#installation) is a tool for dependency management and packaging in Python.  
It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.  
Poetry offers a lockfile to ensure **_repeatable installs_**, and can build your project for distribution.

2. [install pipx](https://github.com/pypa/pipx#install-pipx) using `brew` / `apt` / `pip` / `scoop`

   ##### On macOS

   ```
   brew install pipx
   pipx ensurepath
   ```

   Upgrade pipx with `brew update && brew upgrade pipx`.

   ##### On Linux

   - Ubuntu 23.04 or above

   ```
   sudo apt update
   sudo apt install pipx
   pipx ensurepath
   ```

   - Ubuntu 22.04 or below

   ```
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   ```

   Upgrade pipx with `python3 -m pip install --user --upgrade pipx`.

   ##### On Windows

   - install via [Scoop](https://scoop.sh/)

   ```
   scoop install pipx
   pipx ensurepath
   ```

   Upgrade pipx with `scoop update pipx`.

   - install via pip (requires pip 19.0 or later)

   ```
   # If you installed python using Microsoft Store, replace `py` with `python3` in the next line.
   py -m pip install --user pipx
   ```

3. install poetry

   ```
   pipx install poetry
   ```

4. Ensure poetry uses a python version allowed by `pyproject.toml` _(i.e. `python = ">=3.10.0,<3.11"`)_

   ```
   which python3
   ```

   use the path from there to

   ```
   poetry env use /PATH/TO/python3
   ```

5. install app dependencies

   ```
   poetry install
   ```

6. [Run](https://python-poetry.org/docs/basic-usage/#using-poetry-run) the script with a title for the PDF as a command-line argument
   ```
   python main.py <NEW_PDF_NAME> [URL_1 URL_2 ...] | [<URL_PER_LINE_FILE.txt>]
   ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
