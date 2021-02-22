with open("./do_class.py", encoding="utf-8") as f:
    print(type(f))
    while True:
        content = f.readline()
        if not content:
            break

        print(content)
