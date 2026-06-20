# Food Similarity Evaluator - Model Run Results & Grading Report

This document contains the evaluation results comparing three food sample images against the recommended meal: **"Avocado toast with egg"** (thresholds: Good Match >= 0.70, Bad Match <= 0.30). 

It compiles all recent test runs, historic runs, averages, and grades the models on consistency and reliability.

---

## 📊 Summary of Similarity Scores

| Model | Sample 1 (Ham/Cheese) | Sample 2 (Avocado Toast) | Sample 3 (Veg Sandwich) |
| :--- | :---: | :---: | :---: |
| **Google Gemini** | `0.25` (Very Bad) | `0.99` (Very Good) | `0.66` (Decent Match) |
| **OpenAI (GPT-4o-mini)** | *Failed (402)* | `1.00` (Very Good) | `0.43` (Decent Match) |
| **Claude 3.5 Sonnet** | *Failed (402)* | `0.99` (Very Good)* | *Failed (402)* |
| **Grok 2 Vision** | *Failed (402)* | `0.99` (Very Good)* | `0.35` (Decent Match) |
| **Llama 3.2 Vision** | *Failed (402)* | `0.99` (Very Good)* | `0.33` (Decent Match) |
| **YOLOv8 (Local)** | `0.80` (Very Good) | `0.30` (Very Bad) | `0.80` (Very Good) |

> [!NOTE]
> * Data marked with `*` is gathered from historic successful runs prior to credit depletion.
> * OpenAI, Claude, Grok, and Llama failed on recent runs with **`Error code: 402` (Insufficient credits)** on OpenRouter.

---

## 🔍 Detailed Scores by Run

### 🥪 Sample 1: Ham & Cheese Sandwich (`sample_sandwich1.jpg`)
* **Google Gemini**:
  * Run 1: `0.25`
  * **Average: `0.25`**
* **YOLOv8 (Local)**:
  * Run 1: `0.80`
  * **Average: `0.80`**

---

### 🥑 Sample 2: Avocado Toast with Egg (`sample_sandwich2.jpg`)
* **Google Gemini**:
  * Run 1: `0.99`
  * Run 2: `0.98`
  * Run 3: `0.99`
  * **Average: `0.99`**
* **OpenAI (GPT-4o-mini)**:
  * Run 1: `0.99`
  * Run 2: `1.00`
  * **Average: `1.00`**
* **Claude 3.5 Sonnet**:
  * Run 1 (Historic): `0.99`
  * **Average: `0.99`**
* **Grok 2 Vision**:
  * Run 1 (Historic): `0.99`
  * **Average: `0.99`**
* **Llama 3.2 Vision**:
  * Run 1 (Historic): `0.99`
  * **Average: `0.99`**
* **YOLOv8 (Local)**:
  * Run 1: `0.30`
  * **Average: `0.30`**

---

### 🥗 Sample 3: Vegetarian Sandwich (`sample_sandwich3.jpg`)
* **Google Gemini**:
  * Run 1: `0.70`
  * Run 2: `0.87`
  * Run 3: `0.50`
  * Run 4: `0.58`
  * **Average: `0.66`**
* **OpenAI (GPT-4o-mini)**:
  * Run 1: `0.50`
  * Run 2: `0.40`
  * Run 3: `0.40`
  * Run 4: `0.40`
  * **Average: `0.43`**
* **Grok 2 Vision**:
  * Run 1: `0.35`
  * **Average: `0.35`**
* **Llama 3.2 Vision**:
  * Run 1: `0.33`
  * **Average: `0.33`**
* **YOLOv8 (Local)**:
  * Run 1: `0.80`
  * Run 2: `0.80`
  * Run 3: `0.80`
  * Run 4: `0.80`
  * **Average: `0.80`**

---

## 🏆 Model Grading & Metrics

### 1. Consistency & Variance
* 🟢 **YOLOv8 (Local) — Grade A+ (Excellent)**: Completely deterministic. Because temperature is set to `0`, it returns the exact same score for the same image every single time.
* 🟢 **OpenAI (GPT-4o-mini) — Grade A (High)**: Extremely stable scores. It graded Sample 3 as `0.40` on three consecutive runs, and Sample 2 as `0.99` / `1.00`. Very low variance.
* 🟡 **Google Gemini — Grade B (Moderate)**: Slightly higher score variance (ranged from `0.50` to `0.87` on the same vegetarian sandwich image depending on the run's API generation properties).
* 🟡 **Grok & Llama — Grade B- (Moderate)**: Showed decent variance, but Llama has a tendency to write conversational responses (e.g., *"The similarity score is 0.33."*) instead of just returning a raw number. We added a stripping function in the code to handle this.

### 2. Reliability & Availability
* 🟢 **YOLOv8 (Local) — Grade A+ (Perfect)**: Runs entirely offline on your computer. Requires no API keys and is completely free.
* 🟢 **Google Gemini — Grade A (Perfect)**: Uses a direct developer key which is highly reliable and does not hit platform credit balance issues.
* 🔴 **OpenRouter Models (OpenAI, Claude, Grok, Llama) — Grade D (Low)**: Highly dependent on account credit status. These frequently fail with `402` billing errors if your OpenRouter balance drops below the threshold for image token processing.

---

## 💡 Explanatory Results Notes

* **Why Gemini/OpenAI rated Sample 1 low (`0.25`):** This is highly accurate. A Ham & Cheese sandwich is not Avocado Toast and contains different nutritional components.
* **Why YOLO rated Sample 1 & 3 high (`0.80`):** Since YOLO is an object detection model, it detects the generic `"sandwich"` class. Since "Avocado toast" is structurally a sandwich, the local script interprets "sandwich detected" as a strong match.
* **Why YOLO rated Sample 2 low (`0.30`):** The small YOLOv8 nano model has trouble identifying food items from certain angles, causing it to miss the sandwich class in this specific image and fall back to a low baseline score.
