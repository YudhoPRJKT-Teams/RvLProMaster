#!/bin/bash

api_key=$1

# ANSI colors for better output
GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[33m"
RESET="\e[0m"

if [ -z "${api_key}" ]; then
    echo -e "${YELLOW}[USAGE]${RESET} bash upload.sh <pypi_api_token>"
    exit 1
fi

echo -e "${GREEN}[INFO]${RESET} Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info > /dev/null 2>&1

echo -e "${GREEN}[INFO]${RESET} Building package..."
if ! python3 -m build > /dev/null 2>&1; then
    echo -e "${RED}[ERROR]${RESET} Build failed!"
    exit 1
fi

echo -e "${GREEN}[INFO]${RESET} Uploading to PyPI..."
if ! twine upload --username __token__ --password "${api_key}" dist/*; then
    echo -e "${RED}[ERROR]${RESET} Upload failed!"
    exit 1
fi

echo -e "${GREEN}[INFO]${RESET} Upload successful!"

echo -e "${GREEN}[INFO]${RESET} Cleaning up..."
rm -rf dist/ build/ *.egg-info > /dev/null 2>&1
