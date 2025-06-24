

api_key=$1

if [ -z "${api_key}" ]; then
    echo "Usage: bash setup.sh <api_key>"
    exit 1
fi

echo "[INFO] Delete Oldest Builds"
rm -rf dist/ build/ RvLProMaster.egg-info/ > /dev/null 2>&1
python -m build > /dev/null 2>&1

echo "[INFO] Uploading to PyPI"
twine upload --username __token__ --password "${api_key}" dist/* || {echo "[ERROR] Upload failed"; exit 1;}
echo "[INFO] Upload successfuly"
echo "[INFO] Cleaning up"
rm -rf dist/ build/ RvLProMaster.egg-info/ > /dev/null 2>&1"
