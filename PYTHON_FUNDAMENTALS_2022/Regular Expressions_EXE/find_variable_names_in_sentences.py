import re
sentence = input()
pattern = r"\b_([a-z0-9A-Z]+)\b"
result = re.findall(pattern, sentence)
print(",".join(result))