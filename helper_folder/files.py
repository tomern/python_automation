
def save_file(data, path):
    try:
        f = open(path, "a")
        f.write(data + "\n")
        f.close()
    except Exception:
        print("Could not save file")