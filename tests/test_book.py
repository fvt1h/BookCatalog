import unittest
from books.book import Book

class TestBook(unittest.TestCase):
    def test_book_attributes(self):
        # Membuat objek buku
        my_book = Book("Sapiens", "Yuval Noah Harari", 2011)

        # Memastikan atribut buku berfungsi dengan baik
        self.assertEqual(my_book.title, "Sapiens")
        self.assertEqual(my_book.author, "Yuval Noah Harari")
        self.assertEqual(my_book.year, 2011)

    def test_book_string_representation(self):
        # Membuat objek buku
        my_book = Book("Sapiens", "Yuval Noah Harari", 2011)

        # Memastikan representasi string buku berfungsi dengan baik
        expected_string = "Sapiens oleh Yuval Noah Harari, Terbit tahun 2011"
        self.assertEqual(str(my_book), expected_string)

if __name__ == "__main__":
    unittest.main()
