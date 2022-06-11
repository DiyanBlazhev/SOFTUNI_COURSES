country = input()
tool = input()
difficulty = 0
evaluation = 0


if country == "Russia":
    if tool == "ribbon":
        difficulty = 9.1
        evaluation = 9.4
    elif tool == "hoop":
        difficulty = 9.3
        evaluation = 9.8
    elif tool == "rope":
        difficulty = 9.6
        evaluation = 9

if country == "Bulgaria":
    if tool == "ribbon":
        difficulty = 9.6
        evaluation = 9.4
    elif tool == "hoop":
        difficulty = 9.55
        evaluation = 9.75
    elif tool == "rope":
        difficulty = 9.5
        evaluation = 9.4

if country == "Italy":
    if tool == "ribbon":
        difficulty = 9.2
        evaluation = 9.5
    elif tool == "hoop":
        difficulty = 9.45
        evaluation = 9.35
    elif tool == "rope":
        difficulty = 9.7
        evaluation = 9.15
score = difficulty + evaluation
diff = 20 - score
needed_percentage = (diff / 20) * 100
print(f"The team of {country} get {score:.3f} on {tool}.")
print(f"{needed_percentage:.2f}%")

