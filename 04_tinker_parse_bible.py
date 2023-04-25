import os
import re
import pdb

def extract_verse_lines(filename):
    """
    Extracts all lines between two lines that start with a number followed
    by a colon followed by another number and returns a list of strings
    containing the lines.
    """
    # Open the file and read its contents
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Create a list to store the extracted lines
    extracted_lines = []

    # Loop through each line in the file
    for i, line in enumerate(lines):
        # Check if the line starts with a number followed by a colon followed
        # by another number
        if re.match(r'^\d+:\d+', line.strip()):
            # If the line matches the pattern, start a new list with the line
            line_list = [line.strip()]

            # Loop through the remaining lines until another line matches the pattern
            for j in range(i+1, len(lines)):
                if re.match(r'^\d+:\d+', lines[j].strip()):
                    # If another line matches the pattern, concatenate all non-empty
                    # elements of line_list into a single string and append to the
                    # extracted_lines list
                    extracted_lines.append(' '.join([elem if elem else ' ' for elem in line_list]))
                    break
                else:
                    # If the line doesn't match the pattern, add it to the current list
                    line_list.append(lines[j].strip())

            # If the end of the file is reached, concatenate all non-empty elements of
            # line_list into a single string and append to the extracted_lines list
            else:
                extracted_lines.append(' '.join([elem if elem else ' ' for elem in line_list]))

            extracted_lines[-1] = extracted_lines[-1][:extracted_lines[-1].rfind(' *** ')]

    return extracted_lines


def concatenate_lines(input_file: str, output_file: str) -> None:
    """
    Concatenates all lines in a text file into one line and writes it to a new text file.

    Parameters:
    - file_path (str): the path to the input text file
    - output_path (str): the path to the output text file

    Returns:
    - None
    """
    with open(input_file, 'r', encoding='cp1252', errors='ignore') as f:
        lines = f.readlines()

    concatenated_line = ''.join(lines).replace('\n', '')

    with open(output_file, 'w') as f:
        f.write(concatenated_line)


def write_lines_to_file(lines_tuple, output_file):
    """
    Writes each string in a tuple to a single line in a text file.

    Args:
        lines_tuple (tuple): A tuple of strings to write to the file, where each
            string represents a single line.
        output_file (str): The name of the file to write to.

    Returns:
        None
    """

    # Check if the output file already exists
    if os.path.exists(output_file):
        raise FileExistsError(f"{output_file} already exists.")

    # Open the output file in write mode
    with open(output_file, 'w') as f:
        # Loop through each line in the tuple and write it to the file
        for line in lines_tuple:
            f.write(line + '\n')


def split_string_after_number(file_path):
    # read the text from file
    with open(file_path, 'r') as file:
        text = file.read()
        
    # split the text after every occurrence of a number followed by a colon followed by another number
    pattern = r'\d+:\d+'
    split_text = re.split(pattern, text)
    split_text = [s.strip() for s in split_text]
    split_text = [s for s in split_text if s != '']
    
    # get the substrings that match the pattern
    matches = re.findall(pattern, text)
    
    # concatenate the substrings and the split text into a list
    result = []
    for i in range(len(split_text)):
        result.append(split_text[i])
        if i < len(matches):
            result.append(matches[i])

    
    return result
 


def main():

    input_filename = "kjv_bible.txt"
    temp_1_filename = "kjb_bible_one_line.txt"
    output_filename = "kjv_bible_verses.txt" 

    # Make a one-line version of the bible
    concatenate_lines(input_filename, temp_1_filename)

    # Split text in the one-line file based on occurrence of each verse
    verses_and_numbers = split_string_after_number(temp_1_filename)
    numbers = [number for verses_and_numbers[i] for i in range(0, len(verses_and_numbers, 2)]
    verses = [verse for verses_and_verses[i] for i in range(1, len(verses_and_verses, 2)]
 
    pdb.set_trace()


     
    lines = extract_verse_lines(temp_1_filename)
    write_lines_to_file(lines, output_filename)
    

    print(len(lines))


if __name__ == "__main__":
    main()
