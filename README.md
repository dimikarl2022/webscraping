# Python Web Scraper

A lightweight and modular web scraping library built with Python. This project provides a simple interface for fetching and parsing web content.

## Features

- Clean and modular architecture
- HTML content parsing
- Mock fetcher for testing and development
- Easy-to-use API

## Project Structure

```
├── demo.py                 # Demo script showing usage
├── scraper/               # Main package directory
│   ├── __init__.py       # Package initialization
│   ├── main.py           # Main scraping coordinator
│   ├── parser.py         # HTML content parser
│   └── fetcher.py        # Web content fetcher
```

## Installation

Clone the repository:

```bash
git clone https://github.com/dimikarl2022/python-web-scraper.git
cd python-web-scraper
```

## Usage

Basic usage example:

```python
from scraper import scrape_website

# Scrape a website
url = "https://example.com"
content = scrape_website(url)

# Print extracted content
for item in content:
    print(item)
```

Run the demo script:

```bash
python demo.py
```

## Components

- **WebFetcher**: Handles webpage content retrieval
- **ContentParser**: Parses HTML content and extracts text
- **Main Scraper**: Coordinates fetching and parsing operations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
