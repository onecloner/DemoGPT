system_template = """
Create a code for the instruction using the plan
There are 3 available functions which are "prompt",  "input" and "show".
"input" allows you to get input from the user
"show" allows you to show 
"prompt" is the ai model and it allows you to generate valid responses.
It has 2 fundamental attributes which are system_template and human_template.
They are used to direct the model to generate a valid response.
At least one of them needs to be defined system_template and human_template.
"""

human_template = """
Instruction: Create a translator which translates to any language
Plan:
Let’s think step by step.
1. Get output language from the user 
2. Get source text which will be translated from the user
4. If all the inputs are filled, use langchain to translate text to output language
5. If translated text is ready, return it to the user
Code:
def translate(language,text):
    if language and text:
        return prompt(
            system_template="You are a helpful assistant that can translate text to {{language}}",
            human_template = "This is the text you are supposed to translate: {{text}}",
            language = language,
            text = text)
language = input("Please enter the language you want to translate to")
text = input("Please enter the text you want to translate to")
translated_text = translate(language,text)
show(translated_text)
##########
Instruction: Generate a math teacher which can solve a multiple-choice math problem given the choices
Plan:
Let’s think step by step.
1. Get math question from the user
2. Get choices from the user
3. If all the inputs are filled, use langchain to generate a solution for that question
4. If solution is ready, use langchain to generate multiple choice from the solution.
5. If the choice is ready, return it to the user
Code:
def solve(question, choices):
    if question and choices:
        solution = prompt(
            system_template = "You are a helpful assistant that can solve and explain any multiple math question",
            human_template = "This is the question to solve:{{question}}",
            question = question
        )
        return prompt(
            system_template = "You are a helpful assistant that uses solution to decide the choice for multiple choice math question",
            human_template = "Which choice is the correct for the question according to the solution?\nChoices are {{choices}}, solution is {{solution}} and question is {{question}}",
            question = question,
            solution = solution,
            choices = choices
        )
        
question = input("Please enter the math question you want to solve")
choices = input("Please enter the choices of that question")
choice = solve(question, choices)
show(choice)
##########
Instruction: Generate a system that can generate tweet from hashtags and give a score for the tweet.
Plan:
Let’s think step by step.
1. Get hashtags from the user
2. If hashtags are filled, use langchain to create tweet.
3. If tweet is created, use langchain to generate a score.
4. If score is created, return tweet and score to the user.
Code:
def generate(hashtags):
    if hashtags:
        return prompt(
            system_template = "You are a helpful assistant that can generate tweet from hashtags",
            human_template = "These are the hashtags:{{hashtags}}",
            hashtags = hashtags
        )

def score(tweet):
    if tweet:
        return prompt(
            system_template = "You are a helpful assistant that can generate score for a tweet",
            human_template = "The tweet is:{{tweet}}",
            tweet = tweet
        )
hashtags = input("Enter the hashtags")
tweet = generate(hashtags)
score = score(tweet)
show(score)
##########
Instruction: Create a platform which lets the user select a lecture and then show topics for that lecture 
then give a question to the user. After user gives his/her answer, it gives a score for the answer and give explanation.
Plan:
Let’s think step by step.
1. Use langchain to generate lectures
2. Get lecture from the user among those generated by langchain.
3. After user selects a lecture, generate topics releated to that lecture.
4. Get topic from the user among those generated by langchain.
5. After user selects the topic, use langchain to generate a question related to that topic and lecture
6. Get answer from the user.
7. Use langchain to validate the answer
8. If validation is created, return it to the user.
Code:
def generateLectures():
    return prompt(
            system_template = "You are a helpful assistant that can generate list of lectures"
        )
    
def generateTopics(lecture):
    return prompt(
            system_template = "You are a helpful assistant that can generate list of topics for the lecture",
            human_template = "Generate a list of topics for this lecture:{{lecture}}",
            lecture=lecture
        )
    
def validate(question, answer):
    return prompt(
            system_template = "You are a helpful assistant that reads the answer for the given question coming from student",
            human_template = "Question: {{question}}, Answer: {{answer}}",
            lecture=lecture
        )
    
def generateQuestion(lecture, topic):
    return prompt(
            system_template = "You are a helpful assistant that can generate a question from the topic in the given lecture",
            human_template = "Lecture is {{lecture}}, topic is {{topic}}. Generate a question related to this topic in that lecture"
            lecture=lecture,
            topic=topic
        )

def validateAnswer(question, user_answer, answer):
    return prompt(
            system_template = "You are a helpful assistant that validate user answer by comparing the actual answer to the question",
            human_template = "Question is {{question}}, user gave this answer: {{user_answer}}. The actual answer is {{answer}}"
            question=question,
            user_answer=user_answer,
            answer=answer
        )

lectures = generateLectures()
lecture = input(f"Please select one of the following lectures:{{lectures}}")
topics = generateTopics()
topic = input(f"Please select one of the following topics:{{topics}}")
question = generateQuestion(lecture, topic)
show(question)
user_answer = input("What is the answer?")
validation = validateAnswer(question, user_answer, answer)
show(validation)
##########
Instruction:{instruction}
Plan:
{plan}
Code:
"""
