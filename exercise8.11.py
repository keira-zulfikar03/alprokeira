def send_messages(messages, sent_messages):
    """Print each message and move it to the sent list."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


texts = ['Hello!', 'Are you coming tonight?', 'See you at 7.']
sent_messages = []

send_messages(texts[:], sent_messages)

print("\nOriginal list:", texts)
print("Sent messages:", sent_messages)