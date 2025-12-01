# This script extracts and displays metadata from a specified file.
# It retrieves information such as file size,
# creation date, and last modified date.
import os
from pprint import pprint


def extract_metadata(file_path):
    '''Extracts metadata from the specified file.
       Checks if the file exists before attempting to extract metadata.
       arranges the metadata in a dictionary format,
       and displays it in a readable format.'''
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    metadata = {}
    metadata['File Name'] = os.path.basename(file_path)
    metadata['File Size (bytes)'] = os.path.getsize(file_path)
    metadata['Creation Time'] = os.path.getctime(file_path)
    metadata['Last Modified Time'] = os.path.getmtime(file_path)
    metadata['Absolute Path'] = os.path.abspath(file_path)

    return metadata


# test the function with a sample file path to 'Test File.docx'
if __name__ == "__main__":
    # Sample file path
    file_path = 'Test File.docx'
    # Extract and display metadata, using error handling for file not found
    try:
        metadata = extract_metadata(file_path)
        pprint(metadata)
    except FileNotFoundError as e:
        print(e)
        print("Please check the file path and try again.")
