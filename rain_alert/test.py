import os
from dotenv import load_dotenv

load_dotenv("C:/Users/bento/OneDrive/Documents/Programming/Python/EnvironmentalVariables/.env.txt")
test = os.getenv("test_var")
print(test)