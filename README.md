# Food Similarity Evaluator - Model Run Results & Grading Report

This document contains the evaluation results comparing three food sample images against the recommended target meal: **"Avocado toast with egg"** using the new simplified prompt and integer scoring scale (from `1` to `10`, with thresholds: Good Match >= `7`, Bad Match <= `3`).

It compiles all recent test runs, averages, and grades the models on consistency and reliability.

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

The table below shows the calculated **average similarity scores** across three consecutive runs for each model:

| Model | Type | Sample 1 (Ham/Cheese) | Sample 2 (Avocado Toast) | Sample 3 (Veg Sandwich) |
| :--- | :---: | :---: | :---: | :---: |
| **Qwen2.5-VL (3B)** | Local | `2.00` (Very Bad) | `9.00` (Very Good) | `2.00` (Very Bad) |
| **Moondream (1.8B)** | Local | `1.00` (Very Bad) | `8.00` (Very Good) | `1.00` (Very Bad) |
| **LLaVA (7B)** | Local | `7.33` (Very Good)* | `7.33` (Very Good)* | `4.00` (Decent Match)* |
| **YOLOv8 (Local)** | Local | `8.00` (Very Good)** | `3.00` (Very Bad)** | `8.00` (Very Good)** |
| **Google Gemini 2.5 Flash** | Cloud API | `1.00` (Very Bad) | `10.00` (Very Good) | `4.33` (Decent Match) |

> [!WARNING]
> * **LLaVA** exhibits extremely high score variance across runs (e.g., scoring the Ham/Cheese sandwich anywhere between `5` and `9`, and the actual Avocado Toast match anywhere between `4` and `10`), making its averaged results highly unreliable.
> ** **YOLOv8** is heuristic-based: it detects the generic `"sandwich"` class. Because Ham/Cheese and Veg Sandwich are sandwiches, it scores them high (`8`), but it misses the sandwich in the Avocado Toast image due to angle limitations, scoring it low (`3`).

---

## 🔍 Detailed Scores by Run

### 🥪 Sample 1: Ham & Cheese Sandwich (`sample_sandwich1.jpg`)
* **Qwen2.5-VL (3B)**:
  * Run 1: `2` | Run 2: `2` | Run 3: `2`
  * **Average: `2.00`**
* **Moondream (1.8B)**:
  * Run 1: `1` | Run 2: `1` | Run 3: `1`
  * **Average: `1.00`**
* **LLaVA (7B)**:
  * Run 1: `5` | Run 2: `9` | Run 3: `8`
  * **Average: `7.33`**
* **YOLOv8 (Local)**:
  * Run 1: `8` | Run 2: `8` | Run 3: `8`
  * **Average: `8.00`**
* **Google Gemini**:
  * Run 1: `1` | Run 2: `1` | Run 3: `1`
  * **Average: `1.00`**

---

### 🥑 Sample 2: Avocado Toast with Egg (`sample_sandwich2.jpg`)
* **Qwen2.5-VL (3B)**:
  * Run 1: `9` | Run 2: `9` | Run 3: `9`
  * **Average: `9.00`**
* **Moondream (1.8B)**:
  * Run 1: `8` | Run 2: `8` | Run 3: `8`
  * **Average: `8.00`**
* **LLaVA (7B)**:
  * Run 1: `4` | Run 2: `10` | Run 3: `8`
  * **Average: `7.33`**
* **YOLOv8 (Local)**:
  * Run 1: `3` | Run 2: `3` | Run 3: `3`
  * **Average: `3.00`**
* **Google Gemini**:
  * Run 1: `10` | Run 2: `10` | Run 3: `10`
  * **Average: `10.00`**

---

### 🥗 Sample 3: Vegetarian Sandwich (`sample_sandwich3.jpg`)
* **Qwen2.5-VL (3B)**:
  * Run 1: `2` | Run 2: `2` | Run 3: `2`
  * **Average: `2.00`**
* **Moondream (1.8B)**:
  * Run 1: `1` | Run 2: `1` | Run 3: `1`
  * **Average: `1.00`**
* **LLaVA (7B)**:
  * Run 1: `4` | Run 2: `7` | Run 3: `1`
  * **Average: `4.00`**
* **YOLOv8 (Local)**:
  * Run 1: `8` | Run 2: `8` | Run 3: `8`
  * **Average: `8.00`**
* **Google Gemini**:
  * Run 1: `5` | Run 2: `4` | Run 3: `4`
  * **Average: `4.33`**

---

## 🏆 Model Grading & Metrics

### 1. Consistency & Variance
* 🟢 **YOLOv8 (Local) — Grade A+ (Excellent)**: Completely deterministic. Since it works on heuristic label matches, there is zero variance across runs.
* 🟢 **Qwen2.5-VL (3B) — Grade A+ (Excellent)**: Completely stable (`0.0` variance). Scored `2`, `9`, and `2` respectively on all three runs of each sample. Superb local consistency.
* 🟢 **Moondream (1.8B) — Grade A+ (Excellent)**: Completely stable (`0.0` variance). Scored `1`, `8`, and `1` respectively. Highly consistent and very small/fast.
* 🟢 **Google Gemini — Grade A (High)**: Very stable scores (variance <= `0.33`). Graded Sample 3 as `5`, `4`, `4` across runs.
* 🔴 **LLaVA (7B) — Grade F (Unacceptable)**: Extreme variance across identical runs (e.g. rating Sample 3 as `4`, `7`, then `1`; rating Sample 1 as `5`, `9`, then `8`). Unreliable for automated food adherence grading.

### 2. Reliability & Availability
* 🟢 **Local Models (Qwen, LLaVA, Moondream, YOLO) — Grade A+ (Perfect)**: 100% offline, free, and self-hosted via Ollama. No credit depletion, no API rate limits.
* 🟡 **Google Gemini — Grade B (Moderate)**: Requires active API key and internet connectivity, subject to API availability.
