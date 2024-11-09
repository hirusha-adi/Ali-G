from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": r"Do this in full Ali G style. 100% ali g style. also, dont make it too long, be on point. DO NOT MENTION ANYTHING THATS NOT SAFE FOR WORK (NSFW): A description for a github repository, that will make you sound like ali g. just a one small sentence",
        }
    ],
    # Add any other necessary parameters
)
print(response.choices[0].message.content)
