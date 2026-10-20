text = input("Enter text without spaces: ")
if text == "":
    print("Empty input")
else:
    encoded = ""
    current = text[0]
    count = 1
    for char in text[1:]:
        if char == current:
            count += 1
        else:
            encoded += current + str(count)
            current = char
            count = 1
    encoded += current + str(count)
    print("Original:", text)
    print("Encoded:", encoded)
    print("Original length:", len(text))
    print("Encoded length:", len(encoded))
    if len(encoded) >= len(text):
        print("Compression is not beneficial")
    else:
        print("Compression is beneficial")