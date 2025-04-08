import json
from datetime import datetime

class PersonalLibraryManager:

    def __init__(self, filename="library.json"):
        self.filename = filename
        self.library = self.library_load()


    def library_load(self):
        try:
            with open(self.filename, 'r')as file:
                return json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            return[]
        
    def save_library(self):
        with open(self.filename, 'w')as file:
            json.dump(self.library, file, indent=4)

    def add_book(self):
        while True:     
                title  =  input("Enter book title: ").strip().lower()
                if not title:
                    print("Error:, Please enter book 'Title'.")
                    continue
                author =  input("Enter book author name: ").strip().lower()
                if not author:
                    print("Error:, Please enter 'Author' name.")
                    continue
                
                gener  =  input("Enter the genre: ").strip().lower()
                if not gener:
                    print("Error:, Please enter 'gener' name.")
                    continue
                read   =  input("Have you read this book? (yes/no): ").strip().lower()
                if not read:
                    print("Error:, Please enter 'Read' name.")
                    continue

                if read not in ['yes','no']:
                    print("Error: Please enter 'yes' or 'no' in the Read status.")
                    continue
                read_input = read == 'yes'
        
                while True:
                    date   =  input("Enter the publication year (YYYY-MM-DD): ")
                    try:
                         date_obj = datetime.strptime(date, "%Y-%m-%d")
                    except ValueError:
                         print("Invalid date format. Please inter in YYYY-MM-DD format")
                         continue

                    for book in self.library:
                         if book['Title'].lower() == title.lower() and book['Author'].lower() == author.lower():
                                   
                                   print("This book is already added to the library.")
                                   return
                         
                    book ={
                         "Title": title,
                         "Author": author,
                         "Date":  date,
                         "Gener": gener,
                         "Read": read_input
                    }

                    self.library.append(book)
                    self.save_library()
                    print("Book is added successfully!\n ")
                    break
                break
    def remove_book(self):
        title = input ("Enter book title or author name: ").strip().lower()

        filtered_library = [book for book in self.library if book['Title'].lower() != title.lower() and book['Author'].lower() != title.lower()]
        
        if len(filtered_library)< len(self.library):
             self.library = filtered_library
             self.save_library()
             print("Book is removed Successfuly.")
        else:
             print("Book is not found.")
                
    def display_book(self):
         if not self.library:
            print("Empty book list.")

         for index, book in enumerate(self.library, start=1):
              print(f"{index}. Title: {book['Title']}, Author: {book['Author']}, Read: {'yes' if book['Read'] else 'no'}")

    def display_statics(self):
         if not self.library:
              print("Empty book list.")
         
         total = len(self.library)
         read  = sum([1 for book in self.library if book['Read'] is True])
         print(f"Total: {total}\nBooks Read: {(read/total*100) if total else 0 :.2f}%")

    def search_book(self):
         if not self.library:
              print("Error: Empty book list.")
              return
              
         keyword = input("Enter book title or author name: ")
         if not keyword:
              print("Error: Empty input. Please enter book 'title' or 'author' name." )
              return
         Result = [book for book in self.library if keyword in book['Title'] or keyword in book['Author']]
        
         if Result:
            for index, book in enumerate(Result, start=1):
                print(f"\nSearch Result:\n{index}. Title: {book['Title']}, Author: {book['Author']}, Read: {book['Read']}")
         else:
              print(f"\nSearch Result:\nThe search result for '{keyword}' is not found.")
              

         
    

    def menu(sefl):
         while True:
              print("\nPersonal Library Manager")
              print(f"1. Add Book")
              print(f"2. Remove Book")
              print(f"3. display Book")
              print(f"4. display_statistics")
              print(f"5. Search Book")
              print(f"6. Exite")
              
              choice = input("\nTo perform the operation. Pleanse enter an option(1-6): ")

              if choice == "1":
                   sefl.add_book()
              elif choice == "2":
                   sefl.remove_book()
              elif choice == "3":
                   sefl.display_book()
              elif choice == "4":
                   sefl.display_statics()
              elif choice == "5":
                   sefl.search_book()
              elif choice == "6":
                   print("Exiting a program.Goodbye!")
                   break
              else:
                   ("Invalid Choice.Please emter one of the provided option.")
    

if __name__ == "__main__":
    PersonalLibraryManager().menu()