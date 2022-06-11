count_of_strings = int(input())
special_word = input()
list_of_sentences = []

for i in range(count_of_strings):
    sentence = input()
    list_of_sentences.append(sentence)

print(list_of_sentences)
for i in range(len(list_of_sentences) - 1, -1, -1):
    element = list_of_sentences[i]
    if special_word not in element:
        list_of_sentences.remove(element)

print(list_of_sentences)
