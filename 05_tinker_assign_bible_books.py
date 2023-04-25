import pdb

books = [
    "Genesis", 
    "Exodus", 
    "Leviticus", 
    "Numbers", 
    "Deuteronomy", 
    "Joshua", 
    "Judges", 
    "Ruth", 
    "1 Samuel", 
    "2 Samuel", 
    "1 Kings", 
    "2 Kings", 
    "1 Chronicles", 
    "2 Chronicles", 
    "Ezra", 
    "Nehemiah", 
    "Esther", 
    "Job", 
    "Psalms", 
    "Proverbs", 
    "Ecclesiastes", 
    "Song of Solomon", 
    "Isaiah", 
    "Jeremiah", 
    "Lamentations", 
    "Ezekiel", 
    "Daniel", 
    "Hosea", 
    "Joel", 
    "Amos", 
    "Obadiah", 
    "Jonah", 
    "Micah", 
    "Nahum", 
    "Habakkuk", 
    "Zephaniah", 
    "Haggai", 
    "Zechariah", 
    "Malachi", 
    "Matthew", 
    "Mark", 
    "Luke", 
    "John", 
    "Acts", 
    "Romans", 
    "1 Corinthians", 
    "2 Corinthians", 
    "Galatians", 
    "Ephesians", 
    "Philippians", 
    "Colossians", 
    "1 Thessalonians", 
    "2 Thessalonians", 
    "1 Timothy", 
    "2 Timothy", 
    "Titus", 
    "Philemon", 
    "Hebrews", 
    "James", 
    "1 Peter", 
    "2 Peter", 
    "1 John", 
    "2 John", 
    "3 John", 
    "Jude", 
    "Revelation"
]

def extract_first_number(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                tokens = line.split(":")
                if tokens[0].isdigit():
                    numbers.append(int(tokens[0]))
    return numbers

def repeated_occurrences(lst):
    # Replace all non-one elements with zero
    lst = [1 if x == 1 else 0 for x in lst]
 
    indices = []
    # Find indices for each occurence of 0 then 1
    for i in range(len(lst)-1):
        if lst[i] == 0 and lst[i+1] == 1:
            indices.append(i)
    return indices

def main():
    filename = "kjv_bible_verses.txt"
    numbers = extract_first_number(filename)
    index_start_book = repeated_occurrences(numbers)
    pdb.set_trace() 

if __name__ == "__main__":
    main()