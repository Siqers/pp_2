def snake(text):
    result = [text[0].lower()]
    for char in text[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    return ''.join(result)

# Example usage
camel = str(input())
snake = snake(camel)
print(snake)