# Food Similarity Evaluator - Model Run Results

This document contains the evaluation results comparing three food sample images against the recommended meal: **"Avocado toast with egg"** (thresholds: Good >= 0.7, Bad <= 0.3).

---

## 📊 Summary of Similarity Scores

| Model | Sample 1 (Ham & Cheese Sandwich) | Sample 2 (Avocado Toast with Egg) | Sample 3 (Vegetarian Sandwich) |
| :--- | :---: | :---: | :---: |
| **Google Gemini** | `0.25` (Very Bad) | `0.99` (Very Good) | `0.65` (Decent Match) |
| **YOLOv8 (Local)** | `0.80` (Very Good) | `0.30` (Very Bad) | `0.80` (Very Good) |
| **OpenAI (GPT-4o-mini)** | *Failed (402)* | *Failed (402)* | *Failed (402)* |
| **Claude 3.5 Sonnet** | *Failed (402)* | *Failed (402)* | *Failed (402)* |
| **Grok 2 Vision** | *Failed (402)* | *Failed (402)* | *Failed (402)* |
| **Llama 3.2 Vision** | *Failed (402)* | *Failed (402)* | *Failed (402)* |

> [!NOTE]
> **OpenRouter Billing Status:** All models accessing OpenRouter APIs (OpenAI, Claude, Grok, Llama) failed during these runs with an **`Error code: 402` (Insufficient credits)**. You will need to add credits on your [OpenRouter Billing Settings](https://openrouter.ai/settings/credits) to run these APIs successfully.

---

## 🔍 Detailed Observations

### 1. Google Gemini (`gemini-2.5-flash`)
* **Sample 1:** Gave `0.25`. This is highly accurate since a standard Ham and Cheese sandwich contains none of the key ingredients (avocado, egg) or macro profiles of the target meal.
* **Sample 2:** Gave `0.99`. Outstanding performance. It correctly identified the exact match to "Avocado toast with egg".
* **Sample 3:** Gave `0.65`. Correct grading since it is a sandwich containing vegetables and bread, making it a "decent but not perfect" match.

### 2. YOLOv8 (Local Object Detection)
* **Sample 1 & 3:** Both returned `0.80`. Since YOLO is a local image classifier, it successfully detected the `"sandwich"` class in both images. Because a sandwich shares bread/toast features with "Avocado toast", it is graded as a strong structural match.
* **Sample 2:** Returned `0.30`. The tiny model did not detect standard COCO food bounding boxes on this specific image, resulting in a fallback score.

### 3. OpenRouter Models (OpenAI, Claude, Grok, Llama)
* **Behavior:** Once you add credit, these models will compare the image and return a score. They are set up with a safety parser that cleans trailing punctuation (e.g. converting `"0.33."` to `0.33` successfully) to prevent float conversion errors.
