# Check HSTS

This is a Python script that checks if a website supports HSTS (HTTP Strict Transport Security).

## Installation

1. Clone this repository: `git clone https://github.com/relayhawk/security-scripts`
2. Navigate to the cloned directory: `cd hsts`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (on Windows, use `venv\Scripts\activate`)
5. Install the required packages: `pip install -r requirements.txt`

## Usage

Run the script with the URL to check as the argument:

```bash
python check_hsts.py https://www.website.com
```

If the website supports HSTS, the script will print `HSTS is supported!`. If not, it will print `HSTS is not supported.`.
