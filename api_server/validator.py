def validate_input(text):
    if not text or len(text.strip()) == 0:
        raise ValueError("Input cannot be empty")
    if len(text) > 5000:
        raise ValueError("Input too long")

def validate_output(output):
    if not output:
        return False
    if len(output) < 10:
        return False
    return True