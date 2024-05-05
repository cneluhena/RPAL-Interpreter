import re

def extract_number(input_string):
    match = re.search(r'<INT:(\d+)>', input_string)
    if match:
        return int(match.group(1))
    else:
        return None

# Example usage:
input_string = "<INT:5>"
number = extract_number(input_string)
print(type(number))  