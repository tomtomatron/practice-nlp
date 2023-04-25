import os
import requests
from bs4 import BeautifulSoup

def main():


    # Define the URL for the King James Version of the Bible on the Gutenberg Project website
    url = 'https://www.gutenberg.org/files/10/10-0.txt'

    # Define the filename for the text file
    filename = 'kjv_bible.txt'

    # Check if the file already exists
    if os.path.isfile(filename):
        print('Error: File already exists.')
    else:
        # Send a GET request to the URL to retrieve the text content
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code == 200:

            # Extract the text content from the response using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            text_content = soup.get_text()

            # Save the text content to a file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text_content)
            print('Text file saved successfully.')
        else:
            print('Error: Could not retrieve text content from URL.')


if __name__ == "__main__":
    main()
