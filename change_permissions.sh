# This script changes the permissions of all objects in a folder
# to -rw-r--r-
# Usage: ./change_permissions.sh /path/to/folder

FOLDER_PATH="$1"

if [ -z "$FOLDER_PATH" ]; then
    echo "Error: No folder path provided."
    exit 1
fi

chmod -R 644 "$FOLDER_PATH"
echo "Permissions changed to -rw-r--r- for all objects in $FOLDER_PATH"
echo "Done."
exit 0
