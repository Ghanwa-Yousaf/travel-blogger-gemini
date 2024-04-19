from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## function to load gemini models
## function to get responses
model=genai.GenerativeModel("gemini-pro-vision")


def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text
