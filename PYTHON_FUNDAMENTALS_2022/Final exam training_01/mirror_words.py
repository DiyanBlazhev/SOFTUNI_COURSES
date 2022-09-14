import re
text_string = input()

pattern = r"\@[A-Za-z]{3,}\@{2}[A-Za-z]{3,}\@|\#[A-Za-z]{3,}\#{2}[A-Za-z]{3,}\#"

result = re.findall(pattern, text_string)
if not result:
    print('No word pairs found!')
else:
    print(f"{len(result)} word pairs found!")
new_pattern = r'\@|\#'
mirror_words = {}
for match in result:
    match = re.split(new_pattern, match)
    new_match = filter(lambda x: x != "", match)
    new_match = list(new_match)

    if new_match[0] == new_match[1][::-1]:
        mirror_words[new_match[0]] = new_match[1]

final_list = []
if mirror_words:
    print(f"The mirror words are:")
    for words, mirror in mirror_words.items():
        final_list.append(f"{words} <=> {mirror}")

    print(f"{', '.join(final_list)}")
else:
    print("No mirror words!")




