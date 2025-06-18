questions= [
{
    'question': '1 - What tool is used in containerization?',
    'options': 'A - Docker \nB - AWS \nC - Linux \nD - Terraform',
    'response': 'A'
},

{
    'question': '1 - What tool is used in IaC?',
    'options': 'A - Docker \nB - AWS \nC - Linux \nD - Terraform',
    'response': 'D'
},

{
    'question': '1 - Which is the biggest cloud provider?',
    'options': 'A - Docker \nB - AWS \nC - Linux \nD - Terraform',
    'response': 'B'
}
]

quiz_score = 0

for q in questions:
    print(q.get('question'))
    print(q.get('options'))

    user_choice = input("\nEnter your answer (A, B, C, D): ")

    if user_choice.upper() == q.get('response'):
        print()
        print("You are Right! Good job!!!")
        print()
        quiz_score += 1

    else:
        print("Sorry, wrong answer ;)")

    print("------------------")
print("--------------Result----------")
print(f"You got {quiz_score} out of {len(questions)} correct! {quiz_score*100/len(questions):.2f}%")