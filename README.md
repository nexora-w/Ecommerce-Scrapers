# Inactivity Monitor

A professional application to monitor system inactivity and perform actions.

## Project Structure

- **src/** - Source code files
  - app.py - Main application logic
  - monitor.py - Inactivity monitoring functionality
  - main.py - Entry point
  - signals.py - Signal handling

- **config/** - Configuration files
  - requirements.txt - Python dependencies
  - settings.py - Application settings

- **docs/** - Documentation
  - Detailed project documentation and usage guides

- **tests/** - Test files
  - test_app.py - Unit tests for the application

- **logs/** - Log files (automatically generated)

## Setup

1. Install the required dependencies:
   ```
   pip install -r config/requirements.txt
   ```

2. Run the application:
   ```
   python src/main.py
   ```

## Testing

Run the tests with:
```
python -m unittest discover tests
``` 