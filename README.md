# Hiver Open Challenge — AI Email Suggested Response System

## 🚀 Overview
This project builds an AI system that:
1. **Generates professional email replies** using Google Gemini (Generative AI).
2. **Evaluates replies** with a hybrid accuracy system that balances objective metrics and subjective judgment.
3. Runs **end‑to‑end**: dataset → generation → evaluation → reporting.

---

## 📂 Repository Structure
- `data/sample_emails.json` → dataset of customer queries + ideal replies  
- `dataset_generator.py` → script to generate synthetic dataset  
- `generator.py` → uses Google Gemini to generate replies (few‑shot prompting)  
- `evaluate.py` → computes multi‑metric scores (semantic similarity, politeness, completeness, hybrid score)  
- `judge.py` → Gemini‑as‑judge evaluator (tone, helpfulness, completeness)  
- `main.py` → runs pipeline with CLI options and reports semantic + hybrid + judge scores  
- `results.json` → stores evaluation results  
- `requirements.txt` → dependencies  

---

## 📊 1. Dataset
We created a **synthetic dataset** of customer support emails paired with ideal replies.  
Examples include billing issues, discounts, duplicate charges, and plan upgrades — realistic scenarios that represent common support workflows.  

**Why synthetic?**  
- Public corpora (like Enron) are not customer‑support focused.  
- Hand‑authored examples ensure coverage of **representative support cases**.  
- Small but sufficient for demonstrating the pipeline in 100 minutes.  

---

## 🤖 2. Response Generation
We use **Google Gemini (via Google AI Studio)** to generate replies.  
- Prompting approach: few‑shot examples from dataset guide the model.  
- Trade‑offs:  
  - **Few‑shot prompting** → fast, lightweight, fits challenge time.  
  - **Fine‑tuning** → higher quality but too heavy for 100 minutes.  
  - **RAG** → possible extension, but dataset is small enough for direct prompting.  

---

## 🧠 3. Accuracy & Evaluation
Accuracy for email replies is **not exact match** — good replies can vary in wording.  
We use a **hybrid evaluation system**:

1. **Semantic similarity** (SentenceTransformers `all-mpnet-base-v2`) → checks meaning alignment.  
2. **Politeness check** → ensures professional tone.  
3. **Completeness check** → verifies reply addresses the query.  
4. **Hybrid score** → weighted average: semantic (50%), politeness (25%), completeness (25%).  
5. **Gemini‑as‑judge** → LLM itself rates replies (tone, helpfulness, completeness, 1–5 scale).  

**Why this metric is right:**  
- Captures **meaning** (semantic similarity).  
- Ensures **tone and professionalism** (politeness).  
- Validates **coverage** (completeness).  
- Adds **human‑like judgment** (LLM‑as‑judge).  
Together, this reflects real quality beyond a single number.

---

## 📑 4. Reporting
- **Per‑response scores** → printed in console + saved in `results.json`.  
- **Hybrid score** → reported per response and overall.  
- **Judge scores** → additional qualitative ratings.  
- **Overall scores** → semantic accuracy and hybrid accuracy averages.  

---

## ⚙️ Setup
```bash
git clone <your-repo-url>
cd hiver-open-challenge-advanced
python -m venv venv
.\venv\Scripts\Activate   # Windows PowerShell
pip install -r requirements.txt

Set your Google AI API key:
$env:GOOGLE_API_KEY="your_key_here"

▶️ Run

Generate dataset:
```bash
python main.py --generate

Evaluate replies:
python main.py --evaluate
