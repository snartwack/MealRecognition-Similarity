#imports
import ollama
import os
import re


#variables
script_dir = os.path.dirname(__file__)

#read the sample image number and recommended meal from files in the inputs directory (one level up)
inputs_dir = os.path.join(os.path.dirname(script_dir), "inputs")

# 1. Read active sample number
num_file_path = os.path.join(inputs_dir, "sample_number.txt")
with open(num_file_path, "r") as f:
    sample_num = f.read().strip()

# 2. Read recommended meal text
rec_file_path = os.path.join(inputs_dir, "recommended_meal.txt")
with open(rec_file_path, "r") as f:
    recommended = f.read().strip()

sample_path = os.path.join(inputs_dir, f"sample_sandwich{sample_num}.jpg")
upper_thresh = 7
lower_thresh = 3


#initialization print
print("-----------------------------------\nReady to compare to: " + recommended + "\n-----------------------------------")


#function to compare sample and recommended
def compare_food(image_filename):
    #prompt for moondream to output score from 1 to 10
    prompt = f"""
    Look at the provided image of the consumed meal. Compare it thoroughly with the recommended target meal: {recommended}.
    Provide your output strictly in the following format: Score: [Give a single integer from 1 to 10, where 10 means perfect adherence and 1 means completely different]
    """
    
    #receiving output from local moondream model via Ollama
    response = ollama.chat(
        model="moondream",
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [image_filename]
            }
        ]
    )
    
    text = response["message"]["content"].strip()
    
    # Try to find a number in the response
    for word in text.split():
        clean_word = word.strip(".,;:?![]()\"'")
        try:
            val = int(clean_word)
            if 1 <= val <= 10:
                return str(val)
        except ValueError:
            pass
            
    # Try finding any digits in the text
    digits = re.findall(r'\d+', text)
    for d in digits:
        val = int(d)
        if 1 <= val <= 10:
            return str(val)
            
    # Fallback to 1 (completely different) if empty or no score found
    return "1"


#update print
print(f"Analyzing {sample_path}...\n-----------------------------------")


#try except for actual code
try:
    score = compare_food(sample_path)
    print("SIMILARITY SCORE: " + str(score))
    print("-----------------------------------")
    final = float(score)


    #to judge good or bad match to recommended food
    if final >= upper_thresh:
        print("Very good near perfect match")
    elif final <= lower_thresh:
        print("Very bad match")
    else:
        print("Decent match, not quite recomended")


except Exception as e: #exception catch error and print it
    print("Couldnt analyze" + str(e))
