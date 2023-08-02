def handle_responses(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "hello there"
    