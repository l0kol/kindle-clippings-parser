import numpy as np
import os

save_directory = 'D:/logseq/pages/' #Change this to your logseq directory

def sanitize_filename(name):
    return "".join(c for c in name if c.isalnum() or c in (' ', '.')).rstrip()


#Main loop  
if __name__ == "__main__":
    with open('My Clippings.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()

    books = np.array(data[0::5])
    books = np.unique(books)

    my_books = {}
    for book in books:
        book_notes = []
        book_highlights = []
        for i, line in enumerate(data):
            if line == book:
                if "Your Note" in data[i+1]:
                    book_notes.append(data[i+3])
                elif "Your Highlight" in data[i+1]:
                    book_highlights.append(data[i+3])
        my_books[book] = {'notes': book_notes, 'highlights': book_highlights}






    for book in my_books:
        sanitized_book = sanitize_filename(book)
        file_path = os.path.join(save_directory, sanitized_book + '.md')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('Page auto generated from kindle clippings, #Kindle #books ' '\n')
            f.write('## Highlights\n')
            for highlight in my_books[book]['highlights']:
                #Write each highlight to the file as a new indented line
                f.write('   -  ' + highlight)
            f.write('## Notes\n')
            for note in my_books[book]['notes']:
                f.write('   - ' + note )
