import re

text = "MARIO is Python developer at BiPharmacy, his age is 32"

result = re.findall(r"Mario",text, re.IGNORECASE)
print(result)


result = re.search(r'''(^\w{5})# match 5 letters at start
                    .+(\d{2}$)# match 2 digit number at the end''',
                   text, re.X)
print(result.group(1))
print(result.group(2))