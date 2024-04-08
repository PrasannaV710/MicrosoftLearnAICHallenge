# Add OpenAI library
from openai import AzureOpenAI

deployment_name = 'SDK' 

# Initialize the Azure OpenAI client
client = AzureOpenAI(
        azure_endpoint = 'https://challengeresou9427504834.openai.azure.com/', 
        api_key='',  
        api_version="2023-03-15-preview" #  Target version of the API, such as 2024-02-15-preview
        )
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI?"}
    ]
)
generated_text = response.choices[0].message.content

# Print the response
print("Response: " + generated_text + "\n")