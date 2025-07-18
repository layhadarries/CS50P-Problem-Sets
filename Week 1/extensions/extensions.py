def main():
    file_type = str(input("File name: ").lower().strip(" "))

    if file_type.endswith(".jpeg") or file_type.endswith(".jpg"):
        file("image/jpeg")
    elif file_type.endswith(".png"):
        file("image/png")
    elif file_type.endswith(".gif"):
        file("image/gif")
    elif file_type.endswith(".pdf"):
        file("application/pdf")
    elif file_type.endswith(".txt"):
        file("text/plain")
    elif file_type.endswith(".zip"):
        file("application/zip")
    else:
        file("application/octet-stream")

def file(a):
    print(a)

main()
