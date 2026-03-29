"""
Word Count
Melissa Palmer
This program presents a menu of 4 predefined files and once the user selects the file they want the program will anaylze the file.
Starter code came from 
3/29/2026
"""

from pathlib import Path
import string

class WordAnalyzer:
    
    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        
        self.__frequencies = {}
        
    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError
            
            translator = str.maketrans('','',string.punctuation)
            
            with self.__filepath.open('r') as file:
                for line in file:
                    clean_line = line.translate(translator).lower()
                    
                    words = clean_line.split()
                    
                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        
                    else:
                        self.___frequencies[word] = 1
                        
            return True

        except FileNotFoundError:
            print("Error: File not found.")
            
    def print_report(self):
        sorted_words = sorted(self.__frequencies.keys())
        
        print()
        for word in sorted_words:
            print(f"{word:<6} :: {self.__frequencies[word]}")
            
    
            
            
        
            
        