import openai
from dotenv import dotenv_values

config = dotenv_values("blog.env")

openai.api_key = config["API_KEY"]

def gen_blog(paragraph_topic):
    response = openai.completions.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = "Write a paragraph about the follow topic " + paragraph_topic,
        max_tokens = 400,
        temperature = 0.3
    )
    retrive_blog = response.choices[0].text
    return retrive_blog


keep_writing = True

while keep_writing:
    answer = input("Write a paragraph? Y for yes, anything else for no. ")
    if (answer == "Y"):
        paragraph_topic = input("What should this paragraph talk about? ")
        print(" ")
        print(gen_blog(paragraph_topic))
        print(" ")
    else:
        keep_writing = False