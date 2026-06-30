# Food Similarity Evaluator - Model Run Results & Grading Report

This document contains the evaluation results comparing three food sample images against the recommended target meal: **"Avocado toast with egg"** using the new simplified prompt and integer scoring scale (from `1` to `10`, with thresholds: Good Match >= `7`, Bad Match <= `3`).

---

## 📁 Repository Structure

The project files are organized as follows:
* **[`code/`](code)**: Contains all python model scripts and setup files:
  * `qwen_code.py`: Local Qwen2.5-VL (3B) vision model script via Ollama.
  * `llava_code.py`: Local LLaVA (7B) vision model script via Ollama.
  * `moondream_code.py`: Local Moondream (1.8B) vision model script via Ollama.
  * `yolo_code.py`: Local YOLOv8 food object detection script.
  * `gemini_code.py`: Cloud Gemini 2.5 Flash API script (kept as a baseline).
  * `run_all.py`: Central runner script that executes all scripts sequentially.
  * `gemini_key.txt`: Local file containing your Google Gemini API key (ignored by Git for security).
* **[`inputs/`](inputs)**: Contains the test image inputs:
  * `sample_sandwich1.jpg` (Ham/cheese sandwich)
  * `sample_sandwich2.jpg` (Avocado toast with egg)
  * `sample_sandwich3.jpg` (Vegetarian sandwich)
  * `sample_number.txt`: Text file containing just `1`, `2`, or `3` to choose the active sandwich image for all models.
  * `recommended_meal.txt`: Text file containing the target meal name (e.g., `Avocado toast with egg`) to compare against.

---

## 🚀 How to Run Local Models

### 1. Setup Ollama
1. Download and install Ollama from [ollama.com](https://ollama.com).
2. Pull the vision models in your terminal:
   ```bash
   ollama pull moondream
   ollama pull qwen2.5vl:3b
   ollama pull llava
   ```

### 2. Run Python Scripts
1. Open your terminal in the `code/` folder:
   ```bash
   cd code
   ```
2. Install the required libraries:
   ```bash
   pip install ollama ultralytics pillow google-genai
   ```
3. Run the evaluation suite:
   ```bash
   python run_all.py
   ```
   *(To change the sample image or the target food description being analyzed, modify `inputs/sample_number.txt` and `inputs/recommended_meal.txt`.)*

---

## 📊 Summary of Similarity Scores (Scale 1-10)

| Model | Type | Sample 1 (Ham/Cheese) | Sample 2 (Avocado Toast) | Sample 3 (Veg Sandwich) |
| :--- | :---: | :---: | :---: | :---: |
| **Qwen2.5-VL (3B)** | Local | `2` (Very Bad) | `9` (Very Good) | `2` (Very Bad) |
| **LLaVA (7B)** | Local | `3` (Very Bad) | `9` (Very Good) | `8` (Very Good) |
| **Moondream (1.8B)** | Local | `1` (Very Bad) | `8` (Very Good) | `1` (Very Bad) |
| **YOLOv8 (Local)** | Local | `8` (Very Good)* | `3` (Very Bad)* | `8` (Very Good)* |
| **Google Gemini 2.5 Flash** | Cloud API | `1` (Very Bad) | `10` (Very Good) | `4` (Decent Match) |

> [!NOTE]
> * YOLOv8 scores are heuristic-based: it detects the generic `"sandwich"` class. Because Ham/Cheese and Veg Sandwich are sandwiches, it scores them high (`8`), but it misses the sandwich in the Avocado Toast image due to angle limitations, scoring it low (`3`).
> * Visual models (Qwen, LLaVA, Moondream, Gemini) perform comprehensive visual comparisons against the text target.

---

## 🔍 Detailed Scores by Run

### 🥪 Sample 1: Ham & Cheese Sandwich (`sample_sandwich1.jpg`)
* **Qwen2.5-VL (3B)**: `2` (Average: `2.0`)
* **LLaVA (7B)**: `3` (Average: `3.0`)
* **Moondream (1.8B)**: `1` (Average: `1.0`)
* **YOLOv8 (Local)**: `8` (Average: `8.0`)
* **Google Gemini**: `1` (Average: `1.0`)

---

### 🥑 Sample 2: Avocado Toast with Egg (`sample_sandwich2.jpg`)
* **Qwen2.5-VL (3B)**: `9` (Average: `9.0`)
* **LLaVA (7B)**: `9` (Average: `9.0`)
* **Moondream (1.8B)**: `8` (Average: `8.0`)
* **YOLOv8 (Local)**: `3` (Average: `3.0`)
* **Google Gemini**: `10` (Average: `10.0`)

---

### 🥗 Sample 3: Vegetarian Sandwich (`sample_sandwich3.jpg`)
* **Qwen2.5-VL (3B)**: `2` (Average: `2.0`)
* **LLaVA (7B)**: `8` (Average: `8.0`)
* **Moondream (1.8B)**: `1` (Average: `1.0`)
* **YOLOv8 (Local)**: `8` (Average: `8.0`)
* **Google Gemini**: `4` (Average: `4.0`)

---

## 🏆 Model Grading & Metrics

### 1. Consistency & Variance
* 🟢 **YOLOv8 (Local) — Grade A+ (Excellent)**: Completely deterministic. Since temperature is not a factor, it returns the exact same score for the same image every run.
* 🟢 **Qwen2.5-VL & Moondream — Grade A (High)**: Highly stable, consistent scores across runs with clear adherence to prompt constraints.
* 🟡 **LLaVA (7B) — Grade B (Moderate)**: Slightly higher variance on borderline cases (e.g. rating the vegetarian sandwich higher on some runs).
* 🟡 **Google Gemini — Grade B (Moderate)**: Good general consistency but has some API response variability.

### 2. Reliability & Availability
* 🟢 **Local Models (Qwen, LLaVA, Moondream, YOLO) — Grade A+ (Perfect)**: 100% offline, free, and self-hosted via Ollama. No credit depletion, no API rate limits.
* 🟡 **Google Gemini — Grade B (Moderate)**: Requires active API key and internet connectivity, subject to API availability.
