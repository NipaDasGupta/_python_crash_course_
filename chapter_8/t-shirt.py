'''T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.'''


def make_shirt(size, text_of_a_message):
    """Displays the size of the shirt and the text of the message.

    Args:
        size (str): The size of the shirt.
        text_of_a_message (str): The text of the printed message.
    """
    print(f"\nThe size of the shirt is {size.title()}.")
    print(f"The printed message on the shirt is {text_of_a_message.title()}.")


make_shirt('small', 'alice in wonderland')
make_shirt(size='small', text_of_a_message='alice in wonderland')

"""Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message."""


def make_shirt(size='large', text_of_a_message="I love Python"):
    """Displays the size of the shirt and the text of the message.

    Args:
        size (str): The size of the shirt.
        text_of_a_message (str): The text of the printed message.
    """
    print(f"\nThe shirt size is {size.title()}.")
    print(f"The printed message on the shirt is {text_of_a_message.title()}.")


make_shirt()
make_shirt('medium')
make_shirt(size='small', text_of_a_message='alice in wonderland')
