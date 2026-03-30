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
            
            with self.__filepath.open('r', encoding='utf-8') as file: 
                for line in file:
                    clean_line = line.translate(translator).lower()
                    
                    words = clean_line.split()
                    
                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        
                        else:
                            self.__frequencies[word] = 1

            return True

        except FileNotFoundError:
            print("Error: File not found.")
            return False
            
    def print_report(self):
        sorted_words = sorted(self.__frequencies.keys())
        
        print()
        for word in sorted_words:
            print(f"{word:<6} :: {self.__frequencies[word]}")
            
def main():
        base_path = Path.cwd()
        
        files = {
            
        "1": ("Monte Cristo", base_path / "monte_cristo.txt"),
        "2": ("Princess Mars", base_path / "Princess_maes.txt"),
        "3": ("Tarzan", base_path / "Tarzan.txt"),
        "4": ("Treasure Island", base_path / "treasure_island.txt")
    }
        
        while True:
            
            print("\n--- Word Analyzer ---")
            print("Please select a file to analyze:")
            
            for key, (name, _) in files.items():
                print(f"{key}. {name}")
                
            print("5. Exit\n")
            
            choice = input("Enter your choice (1-5):")
            
            if choice == "5":
                
                print("\nGoodbye!")
                break
            
            elif choice not in files:
                print("\nInvalid choice. Please select from 1-5.")
                print("\nPress Enter to return to the menu... ")
                
            else:
                name, filepath = files[choice]
                print("Trying to open:", filepath)
                print(f"\nProcessing '{filepath.name}'...\n")
                
                analyzer = WordAnalyzer(filepath)
                
                if analyzer.process_file():
                    analyzer.print_report()
                    
                    input("\nPress Enter to return to the menu...")
                
            
if __name__ == "__main__":
    main()
        
            
        