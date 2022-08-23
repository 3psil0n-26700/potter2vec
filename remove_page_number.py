# remove page number
for i in range(2,8):
    with open(f"./harry_potter/Book{i}.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    with open(f"./harry_potter/Book{i}.txt", 'w', encoding='utf-8') as f:
        for line in lines:
            if 'Page | ' not in line:
                f.write(line) 