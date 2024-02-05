text = '''TISB is proud to announce the first edition of tisb debate on 17th and 18th february, 2024. it aims to be india’s largest student-led debate competition. Students from around asia will compete to win exciting prizes in thought-provoking debate about crucial world issues and current affairs.

This event will challenge young minds to confront the status quo, while allowing for them to hone skills such as public speaking, quick, analytical problem solving and astute articulation. This online conference welcomes student teams of grades 6-12, aiming to enkindle a voracious curiosity for knowledge beyond classroom material. This will cultivate and advance the holistic nature of education that contemporary schools aspire to inculcate.'''

paras = text.split("\n\n")
words = [para.split(' ') for para in paras]
wlens = [[len(word) for word in para] for para in words]
indent = 16
sum_ = 0
for i, para in enumerate(words):
    for j, word in enumerate(para):
        if sum_ >= 128-indent:
            print("\n" + indent*" ", end="")
            sum_ = 0
        sum_ += wlens[i][j]
        print(word, end=" ")
    sum_ = 0
    print("\n" + indent*" " + "<br><br>\n" + indent*" ", end="")
