'''Message: Write a function called display_message() that prints one sentence
telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.'''


def display_message():
    """Display a simple message."""
    print("You are learning about function in this chapter.")


display_message()


def show_messages(text_messages, sent_messages):
    """Show a simple message from a list."""
    print("\nPreview messages before sending:")
    while text_messages:
        unsend_messages = text_messages.pop()
        print(f"{unsend_messages}")
        sent_messages.append(unsend_messages)


def send_messages(sent_messages):
    """Send a message."""
    print("\nThe following messages are being sent:")
    for message in sent_messages:
        print(message)


text_messages = ['hi, dude', 'good morning', 'night']
sent_messages = []

show_messages(text_messages[:], sent_messages)
send_messages(sent_messages)
