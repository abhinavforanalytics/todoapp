import json

with open('Questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)


for ques in data:
    print(ques['Question'])
    for ind, alt in enumerate(ques['Alternatives']):
        print(ind + 1, alt)
    user_choice = int(input("Enter your answer: "))
    ques['user_choice'] = user_choice


score = 0
for ind,ques in enumerate(data):
    if ques['user_choice'] == ques['Correct Answer']:
        score += 1
        result = "Correct Answer!"
    else:
        result = "Wrong Answer."
    message = f"{ind+1}, {result}- Your Answer: {ques['user_choice']}, "\
    f"Correct Answer: {ques['Correct Answer']}"
    print(message)
print("Score: ", score / len(data) * 100, "%")