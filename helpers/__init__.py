def get_full_text(path: str):
    with open(path, "r") as f:
        output = f.read()
    return output


def full_text_to_list(text: str, element_type=str):
    output = text.split("\n")
    if element_type is not str:
        output = [element_type(i) for i in output]
    return output
