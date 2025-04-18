# Pseudomatic

Pseudomatic is a Python-based tool for generating pseudonyms based on a seed string and a selected language. It is useful for anonymizing data or creating unique, repeatable pseudonyms.

## Features

- Supports multiple languages:
  - English (`en`)
  - Ukrainian (`ua`)
- Generates pseudonyms in the format: `Adjective Noun` (e.g., "Brave Fox" or "Хоробрий Лис").
- Deterministic output: the same seed and language will always produce the same pseudonym.
- Supports random pseudonym generation when no seed is provided.

## Installation

### From PyPI

```bash
pip install pseudomatic
```

### From Source

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pseudomatic
   ```

2. Install in development mode:
   ```bash
   pip install -e .
   ```

## Usage

### As a Python Package

```python
from pseudomatic import pseudonym

# Generate a pseudonym in English
pseudonym_en = pseudonym("JohnDoe", language="en")
print(pseudonym_en)  # Example: "Brave Fox"

# Generate a pseudonym in Ukrainian
pseudonym_ua = pseudonym("JohnDoe", language="ua")
print(pseudonym_ua)  # Example: "Хоробрий Лис"

# Generate a random pseudonym (no seed provided)
random_pseudonym = pseudonym(language="en")
print(random_pseudonym)  # Example: "Curious Elephant"

# Generate a random pseudonym in Ukrainian
random_pseudonym_ua = pseudonym(language="ua")
print(random_pseudonym_ua)  # Example: "Цікавий Слон"

# Use different themes
business_pseudonym = pseudonym("JohnDoe", language="en", theme="business")
retail_pseudonym = pseudonym("JohnDoe", language="ua", theme="retail")
```

### From Command Line

Run the script directly:
```bash
python -m pseudomatic
```

This will generate example pseudonyms in English and Ukrainian using the 'retail' theme.

## Project Structure

- `pseudomatic.py`: Main script for generating pseudonyms.
- `names.py`: Contains adjective and noun lists for supported languages.
- `pyproject.toml`: Package configuration for building and distribution.
- `README.md`: Project documentation.

## Development and Deployment

### Continuous Integration/Continuous Deployment

This project uses GitHub Actions for CI/CD:

- When a new release is created on GitHub, the package is automatically built and published to PyPI.
- The workflow is defined in `.github/workflows/publish.yml`.

### Creating a New Release

To create a new release:

1. Update the version number in `pyproject.toml`.
2. Create a new release on GitHub with a tag matching the version (e.g., `v0.1.0`).
3. The GitHub Actions workflow will automatically build and publish the package to PyPI.

### PyPI Authentication

The GitHub Actions workflow requires a PyPI API token stored as a GitHub secret named `PYPI_API_TOKEN`. To set this up:

1. Create an API token on PyPI (https://pypi.org/manage/account/token/).
2. Add the token as a secret in your GitHub repository settings.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
