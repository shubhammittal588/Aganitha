# PubMed Paper Fetcher

## Overview
PubMed Paper Fetcher is a Python module and command-line tool that retrieves research papers from PubMed based on a user-specified query. It identifies papers where at least one author is affiliated with a pharmaceutical or biotech company and saves the results as a CSV file.

## Output
![Screenshot 2025-03-17 at 8 58 07 PM](https://github.com/user-attachments/assets/07807607-9a9a-4c93-a7a4-0b8dd4f99a00)


## Features
- Fetches research papers using the PubMed API.
- Filters papers with at least one non-academic (pharma/biotech) author.
- Saves results in CSV format with the following details:
  - PubMed ID
  - Title
  - Publication Date
  - Non-Academic Author(s)
  - Company Affiliation(s)
  - Corresponding Author Email
- Supports command-line options for flexible usage.
- Uses Poetry for dependency management.
- Published as a module on TestPyPI for easy installation.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Poetry (for dependency management)

### Install from TestPyPI
```sh
pip install --index-url https://test.pypi.org/simple/ pubmed-fetcher
```

### Clone the Repository (For Development)
```sh
git clone https://github.com/yourusername/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

### Install Dependencies
```sh
poetry install
```

## Code Organization
```
├── pubmed_fetcher/          # Main module
│   ├── __init__.py         # Module initialization
│   ├── fetch.py            # Fetching logic
│   ├── utils.py            # Utility functions
│   └── cli.py              # Command-line entry point
├── tests/                   # Unit tests
├── README.md                # Documentation
├── pyproject.toml           # Poetry configuration
├── results.csv              # Example output file
└── outputs/                 # (Optional) Folder for CSV results
```

## Usage
### Running as a CLI Tool
To fetch papers based on a query:
```sh
get-papers-list "cancer treatment"
```

### Command-Line Options
| Option       | Description                                      |
|-------------|-------------------------------------------------|
| `-h, --help` | Show usage instructions.                        |
| `-d, --debug` | Print debug information during execution.      |
| `-f, --file`  | Specify a filename to save the results as CSV. |

### Example Commands
Fetch papers on diabetes research and print output:
```sh
get-papers-list "diabetes research"
```

Fetch papers and save results to a CSV file:
```sh
get-papers-list "gene therapy" -f results.csv
```

Enable debug mode for troubleshooting:
```sh
get-papers-list "cancer treatment" -d
```

## Tools and Libraries Used
- **PubMed API (Entrez Programming Utilities)**: [NCBI PubMed API](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- **Biopython** (for PubMed API interaction): [Biopython](https://biopython.org/)
- **Poetry** (for dependency management): [Poetry](https://python-poetry.org/)

## Publishing to TestPyPI
To build and publish the package:
```sh
poetry build
poetry publish -r testpypi
```

## Troubleshooting
If you encounter SSL certificate issues, try:
```sh
pip install --upgrade certifi
export SSL_CERT_FILE=$(python -m certifi)
```
For Mac users:
```sh
brew install openssl
export SSL_CERT_FILE=$(brew --prefix openssl)/etc/openssl@1.1/cert.pem
```

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to your branch: `git push origin feature-name`
5. Submit a pull request.

## License
This project is licensed under the MIT License.


