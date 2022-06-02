with open('template.md', 'w') as f:
    for i in range(0, 103):
        f.write(f"[![](images/{i}.jpeg)](images/{i}.jpeg)\n")
        f.write(f"<Caption>\n")
        f.write(f"Image {i}:\n")
        f.write(f"</Caption>\n\n")
