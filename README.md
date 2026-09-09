# 🌱 Crop Disease Detection & Management using AI

AI-powered crop leaf disease detection using Vision Transformer, IBM Granite 4.1:3B, knowledge base, and IndicTrans2 translation (English / Hindi / Gujarati).

Built as part of the **AI for Sustainability Virtual Internship** (1M1B × AICTE × IBM SkillsBuild).

---

## Local Setup Guide

Follow these steps to run the application on your machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Viren501/crop_health_ai.git
cd crop_health_ai
```

### 2. Create and Activate Virtual Environment

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

If the `ollama` package is missing:

```bash
pip install ollama
```

### 4. Install Ollama and Pull IBM Granite

1. Download and install Ollama from: https://ollama.com/
2. Pull the Granite model:

```bash
ollama pull granite4.1:3b
```

3. Verify the model is available:

```bash
ollama list
```

You should see `granite4.1:3b` in the list.

Optional test:

```bash
ollama run granite4.1:3b
```

### 5. IndicTrans2 Compatibility Fix (Important)

The IndicTrans2 model may fail to load due to deprecated ONNX imports in its cached configuration file when using newer versions of Transformers.

**Apply this one-time fix after the model is first downloaded:**

1. Locate the cached configuration file (path may vary slightly):

```bash
# Typical location (replace the hash if different)
nano ~/.cache/huggingface/modules/transformers_modules/ai4bharat/indictrans2_hyphen_en_hyphen_indic_hyphen_dist_hyphen_200M/173b94239f7c38886b2747b8d4a5db771a7e1232/configuration_indictrans.py
```

2. Comment out these two lines:

```python
# from transformers.onnx import OnnxConfig, OnnxSeq2SeqConfigWithPast
# from transformers.onnx.utils import compute_effective_axis_dimension
```

3. Save and close the file.

> **Note:** This is a local cache workaround. If you clear the Hugging Face cache or re-download the model, you may need to apply the fix again.

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually http://localhost:8501) in your browser.

---

## Quick Checklist

- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] `pip install -r requirements.txt` completed
- [ ] Ollama installed and `granite4.1:3b` pulled
- [ ] IndicTrans2 deprecated import fix applied (if needed)
- [ ] `streamlit run app.py` started successfully

---

## Supported Features (for reference)

- Upload leaf image (JPG / JPEG / PNG)
- Disease detection with confidence score (Corn, Potato, Rice, Wheat)
- Knowledge-grounded management guidance via IBM Granite
- Language selection: English, Hindi (हिंदी), Gujarati (ગુજરાતી)

---

## Troubleshooting

| Issue | Possible Fix |
|-------|--------------|
| Ollama model not found | Run `ollama pull granite4.1:3b` again |
| IndicTrans2 import error | Apply the compatibility fix in Step 5 |
| Port already in use | Use `streamlit run app.py --server.port 8502` |
| Model download slow | First run downloads Hugging Face models; wait for completion |

---

**Student:** Viren Vairagi  
**Internship:** AI for Sustainability Virtual Internship (1M1B × AICTE × IBM SkillsBuild)
