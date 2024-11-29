"""Assignment week-5"""

class bookStore():
    """A class representing a bookstore.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
    """

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        
    def info(self):
        """
        Returns:
            str: A string containing the book's title, author, and publication year.
        """
        return f"\"Book Title\": {self.title}, \"Author Name\": {self.author}, \"Publication Year: {self.year}\""
    
book = bookStore('The Hidden City', 'MacGregor', '1994')
print(book.info())
