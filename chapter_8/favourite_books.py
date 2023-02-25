''' Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.'''


def favorite_book(book_title):
    """Display the favorite book title."""
    print(f"One of my favorite books is {book_title.title()}.")


favorite_book('alice in wonderland')


def alt_favorite_book(book_title='alice in wonderland'):
    """Display the favorite book title."""
    print(f"One of my favorite books is {book_title.title()}.")


alt_favorite_book()
alt_favorite_book('python crash course')
