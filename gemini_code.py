#imports
from google import genai
import PIL.Image
import os


#variables
script_dir = os.path.dirname(__file__)


#google gemini api key setup
key_path = os.path.join(script_dir, "gemini_key.txt")
with open(key_path, "r") as f:
    api = f.read().strip()
client = genai.Client(api_key=api)

#read the sample image number from sample_number.txt
num_file_path = os.path.join(script_dir, "sample_number.txt")
with open(num_file_path, "r") as f:
    sample_num = f.read().strip()

sample_path = os.path.join(script_dir, f"sample_sandwich{sample_num}.jpg")
recommended = "Avocado toast with egg"
upper_thresh = 0.7
lower_thresh = 0.3


#initialization print
print("-----------------------------------\nReady to compare to: " + recommended + "\n-----------------------------------")




#function to compare sample and recommended
def compare_food(image_filename):
    sample = PIL.Image.open(image_filename)
    #prompt for google gemini to output number from [0,1] (prompt made by ai)
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
    #receiving gemini output and returning
    response = client.models.generate_content(model='gemini-2.5-flash', contents=[sample, prompt])    
    return response.text.strip()#(.strip just to remove whitespace)


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
