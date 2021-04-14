from translate import Translator

trans = Translator(to_lang="Russian")


with open("new_file.txt", "w", encoding="utf-8") as new:
    with open("text_4.txt", "r", encoding="utf-8") as file:
        for line in file:
            word_rus = trans.translate(line.split()[0])
            print(f"{word_rus} {' '.join(line.split()[1:])}", file=new)
