with open('test.txt', 'w') as f: #w, r, a (append)
    f.write("\nimage: nginx")

with open('test.txt', 'r') as r:
    content = r.read()
    print(content)

with open('test.txt', 'r') as r:
    content = r.readlines()
    print(content)

with open('test.txt', 'w') as c:
    for line in content:
        if 'image' in line:
            c.write("image: httpd")
        else:
            c.write(line)