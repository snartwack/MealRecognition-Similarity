#imports
from ultralytics import YOLO
import os


#variables
script_dir = os.path.dirname(__file__)

#read the sample image number from sample_number.txt in the inputs directory (one level up)
inputs_dir = os.path.join(os.path.dirname(script_dir), "inputs")
num_file_path = os.path.join(inputs_dir, "sample_number.txt")
with open(num_file_path, "r") as f:
    sample_num = f.read().strip()

sample_path = os.path.join(inputs_dir, f"sample_sandwich{sample_num}.jpg")
recommended = "Avocado toast with egg"
upper_thresh = 0.7
lower_thresh = 0.3


#initialization print
print("-----------------------------------\nReady to compare to: " + recommended + "\n-----------------------------------")




#function to compare sample and recommended using local object detection
def compare_food(image_filename):
    # Load YOLOv8 model (downloads 'yolov8n.pt' if not present)
    model = YOLO("yolov8n.pt")
    
    # Run prediction
    results = model(image_filename, verbose=False)
    
    # Get detected labels in the image
    detected = []
    for r in results:
        for c in r.boxes.cls:
            label = model.names[int(c)]
            detected.append(label)
            
    # Simple check: does what we detected match the recommended food?
    # Avocado toast with egg has bread/toast/sandwich.
    rec_lower = recommended.lower()
    
    # If the user recommended food contains toast/sandwich/bread, and we detect 'sandwich'
    if ("sandwich" in detected) and ("toast" in rec_lower or "sandwich" in rec_lower or "bread" in rec_lower):
        return "0.8"
    
    # Check other simple COCO food matches (banana, apple, orange, broccoli, carrot, hot dog, pizza, donut, cake)
    for item in ["apple", "banana", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake"]:
        if (item in detected) and (item in rec_lower):
            return "1.0"
            
    # If some food was detected but doesn't match the recommended food
    for item in ["sandwich", "apple", "banana", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake"]:
        if item in detected:
            return "0.3"
            
    return "0.0"


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
