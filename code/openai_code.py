#imports
from openai import OpenAI
import base64
import os


#variables
script_dir = os.path.dirname(__file__)


#openrouter api key setup (using openrouter to access openai)
key_path = os.path.join(script_dir, "openrouter_key.txt")
with open(key_path, "r") as f:
    api = f.read().strip()
client = OpenAI(
    api_key=api,
    base_url="https://openrouter.ai/api/v1"
)

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
upper_thresh = 0.7
lower_thresh = 0.3


#initialization print
print("-----------------------------------\nReady to compare to: " + recommended + "\n-----------------------------------")


#helper function to convert image to base64 text for openrouter
def encode_image(image_filename):
    with open(image_filename, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


#function to compare sample and recommended
def compare_food(image_filename):
    base64_image = encode_image(image_filename)
    #prompt for openai to output number from [0,1] (prompt made by ai)
    prompt = f"""
    You are a nutrition coach.
    Recommended Meal: {recommended}
   
    Look at this image. Compare it to the Recommended Meal based on:
    Ingredients/Macros (Protein, Fats, Carbs)
    Total Calories
    Fiber Content
    Micronutrient Density
    Food Quality
    Processing Level
    Hydration
    Bioavailability
    Satiety Index
    Gut Microbiome Impact
    Glycemic Load
    Antinutrients
    Toxins
    Mindful Eating
    Environment
    Food Matrix
    Bioactive Compounds
    Phytochemicals
    Essential Fatty Acid Balance
    Omega-3 Ratio
    Endocrine Response
    Insulin Sensitivity
    Chemical Additives
    Pesticide Residue
    Hormone Regulation
    Enzymatic Function
    Inflammatory Markers
    Salt Concentration
    Oxidative Stress
    Amino Acid Profile
    Prebiotic Density
    Probiotic Content
   
    Give a similarity score from 0.0 to 1.0.
    1.0 is a perfect match. 0.0 is completely different.
    Return ONLY the number. No words.
    """
    #receiving openai output and returning
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=30
    )
    
    # Extract the score from the response
    text = response.choices[0].message.content.strip()
    
    # Try to find a number in the response
    for word in text.split():
        clean_word = word.strip(".,;:?!")
        try:
            float(clean_word)
            return clean_word
        except ValueError:
            pass
            
    return text


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
