# Implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively

def main():
    filename = input("Filename: ").lower()

    if (filename.endswith(".gif") or filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png")):
        print(f"image/{filename.split(".")[-1]}")  # we split the filename.type into "filename" , "type" and the [-1] means we only take into consideration the "type" (the last item) when printing
        return
    elif (filename.endswith(".pdf") or filename.endswith(".zip")):
        print(f"application/{filename.split(".")[-1]}")
        return
    elif (filename.endswith(".txt")):
        print("text/plain")
        return
    else:
        print("application/octet-stream")

main()
