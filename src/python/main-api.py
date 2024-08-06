import requests
import json

# define endpoint for ollama api
url = "http://localhost:11434/api/generate"

# define headers
headers = {
    'Content-Type': 'application/json',
}

# define function to generate response from ollama api
def generate_response(prompt):
    data = {
        "model": "phi3",
        "stream": False,
        "prompt": prompt,
    }

    # make a post request to the ollama api
    response = requests.post(url, 
                             headers=headers, 
                             data=json.dumps(data))

    # check if the response is successful
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        print("Response: ", actual_response)
    # if the response is not successful, print the error
    else:
        print("Error:", response.status_code, response.text)        
    
generate_response("Why is the sky blue?")