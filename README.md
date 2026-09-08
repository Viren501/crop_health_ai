# 🌱 Crop Disease Detection & Management using AI

An AI-powered crop disease detection and management application that combines **Computer Vision, a structured agricultural knowledge base, IBM Granite, and multilingual translation** to identify supported crop-leaf conditions and provide understandable management and prevention guidance.

This project was developed as part of the **AI for Sustainability Virtual Internship offered by 1M1B in collaboration with AICTE and co-certified by IBM SkillsBuild**.

---

## 📌 Project Overview

Crop diseases can negatively affect agricultural productivity and crop health. Early identification and access to understandable management information can help users become aware of potential crop-health problems.

This project demonstrates an AI-based workflow in which a user can:

- Upload an image of a crop leaf.
- Detect a supported crop condition using a pretrained Vision Transformer (ViT).
- View the predicted condition and confidence score.
- Retrieve relevant agricultural information from a structured knowledge base.
- Use **IBM Granite 4.1:3B** to generate structured management and prevention guidance.
- Select **English, Hindi (हिंदी), or Gujarati (ગુજરાતી)**.
- Translate the generated guidance into the selected language.
- View the complete result through a Streamlit web application.

The project focuses on demonstrating how multiple AI technologies can be combined to address a practical **AI for Sustainability** problem in agriculture.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Detect supported crop-leaf conditions from images.
2. Provide prediction confidence to the user.
3. Provide structured agricultural management information.
4. Use a knowledge-grounded approach for generative AI.
5. Use IBM Granite as the generative AI component.
6. Provide multilingual guidance.
7. Make the application simple to use through Streamlit.
8. Demonstrate an AI application related to sustainable agriculture.
9. Create a modular architecture that can be extended in the future.

---

## 🌾 Supported Crops and Conditions

The project is designed around the following crop categories:

| Crop      | Conditions                                        |
| --------- | ------------------------------------------------- |
| 🌽 Corn   | Common Rust, Gray Leaf Spot, Leaf Blight, Healthy |
| 🥔 Potato | Early Blight, Late Blight, Healthy                |
| 🌾 Rice   | Brown Spot, Leaf Blast, Healthy                   |
| 🌾 Wheat  | Brown Rust, Yellow Rust, Healthy                  |

### Crop Coverage

**4 crop types**

### Listed Conditions

- Corn — 4 conditions
- Potato — 3 conditions
- Rice — 3 conditions
- Wheat — 3 conditions

**Total listed crop conditions: 13**

> ⚠️ **Important:** The project's intended scope and the actual prediction classes of the loaded pretrained model should be kept consistent. The application can only predict labels that are actually present in the model's configuration. The model also contains an `Invalid` class for unsupported/unrecognized images.

---

## 🧠 AI Architecture

The application separates image classification, agricultural information retrieval, text generation, and translation into different components.

```text
                    ┌──────────────────┐
                    │   Leaf Image     │
                    └────────┬─────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │ Vision Transformer (ViT) │
                │ Disease Classification   │
                └────────────┬─────────────┘
                             │
                             ▼
                      Crop + Condition +
                       Confidence Score
                             │
                             ▼
                ┌──────────────────────────┐
                │ Agricultural Knowledge   │
                │ Base                     │
                │ diseases.json            │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │ IBM Granite 4.1:3B       │
                │ Guidance Generation      │
                └────────────┬─────────────┘
                             │
                             ▼
                      English Guidance
                             │
                             ▼
                ┌──────────────────────────┐
                │ IndicTrans2 Model        │
                │ Translation              │
                └────────────┬─────────────┘
                             │
                    ┌────────┼─────────┐
                    ▼        ▼         ▼
                  English   Hindi    Gujarati
                             हिंदी       ગુજરાતી
```

### 🔍 Disease Detection Model

The project uses the pretrained Hugging Face model:

**`wambugu71/crop_leaf_diseases_vit`**

The model is a Vision Transformer-based image-classification model for crop disease detection.

**Base Model:** `WinKawaks/vit-tiny-patch16-224`

The pretrained model is used directly.

#### No Fine-Tuning

This project does **not** fine-tune the disease detection model.

The pretrained model is loaded and used for inference.

This approach reduces the computational requirements of the project and allows the application to focus on integrating multiple AI components.

### 🤖 IBM Granite 4.1:3B

The generative AI component of the project uses:

**IBM Granite 4.1:3B**

Granite is responsible for generating a clear and structured explanation based on the disease prediction and information retrieved from the agricultural knowledge base.

The model receives information such as:

- Crop
- Detected Condition
- Confidence Score
- Description
- Management Information
- Prevention Information

It then generates user-friendly guidance containing sections such as:

- Diagnosis
- What it means
- What to do
- Prevention
- Important note

#### Why IBM Granite?

IBM Granite is used as the IBM component of this project and demonstrates the integration of IBM's generative AI technology into an AI-for-Sustainability application.

### 📚 Agricultural Knowledge Base

The project contains a structured knowledge base:

```
knowledge/
└── diseases.json
```

The knowledge base provides information related to supported crop conditions.

Typical information includes:

- Description
- Management
- Prevention

**Example:**

```json
{
  "Potato___Early_Blight": {
    "crop": "Potato",
    "disease": "Early Blight",
    "description": "Description of the condition.",
    "management": [
      "Management recommendation 1",
      "Management recommendation 2"
    ],
    "prevention": [
      "Prevention recommendation 1",
      "Prevention recommendation 2"
    ]
  }
}
```

#### Why Use a Knowledge Base?

The project does not rely entirely on the LLM's internal knowledge for agricultural recommendations.

Instead:

```
Disease Prediction
        ↓
Knowledge Retrieval
        ↓
Relevant Agricultural Information
        ↓
IBM Granite
        ↓
Structured Explanation
```

This approach helps reduce unsupported or fabricated recommendations.

### 🌐 Multilingual Support

The application supports:

- English
- Hindi (हिंदी)
- Gujarati (ગુજરાતી)

The language can be selected directly from the Streamlit interface.

#### Translation Workflow

```
Leaf Image
    ↓
Disease Detection
    ↓
Knowledge Retrieval
    ↓
IBM Granite
    ↓
English Guidance
    ↓
IndicTrans2
    ↓
Selected Language
```

If English is selected, the Granite response is displayed directly.

If Hindi or Gujarati is selected, the English response is translated before being displayed.

### 🔤 IndicTrans2 Translation Model

The project uses the AI4Bharat IndicTrans2 model for English-to-Indic language translation.

**Model:** `ai4bharat/indictrans2-en-indic-dist-200M`

The model is used for translating the generated English agricultural guidance into supported Indian languages.

Current target languages include:

- Hindi
- Gujarati

### 🔧 IndicTrans2 Local Compatibility Fix

During local setup, the IndicTrans2 model produced a compatibility issue related to deprecated imports in its cached `configuration_indictrans.py` file.

The affected file was located inside the Hugging Face cache:

```
~/.cache/huggingface/modules/transformers_modules/ai4bharat/indictrans2_hyphen_en_hyphen_indic_hyphen_dist_hyphen_200M/173b94239f7c38886b2747b8d4a5db771a7e1232/configuration_indictrans.py
```

The file was opened using:

```bash
nano ~/.cache/huggingface/modules/transformers_modules/ai4bharat/indictrans2_hyphen_en_hyphen_indic_hyphen_dist_hyphen_200M/173b94239f7c38886b2747b8d4a5db771a7e1232/configuration_indictrans.py
```

The following deprecated imports were commented out:

```python
# from transformers.onnx import OnnxConfig, OnnxSeq2SeqConfigWithPast
# from transformers.onnx.utils import compute_effective_axis_dimension
```

#### Why was this required?

The cached IndicTrans2 configuration referenced older/deprecated Transformers ONNX imports.

The project environment uses a newer version of the Transformers ecosystem, resulting in a compatibility issue.

Commenting out these imports allowed the configuration to load successfully in the local environment.

#### Important Reproducibility Note

This modification is a **local compatibility workaround**.

It modifies a file inside the local Hugging Face cache and is **not** part of the GitHub repository source code.

Therefore, if the model is downloaded again or the Hugging Face cache is cleared, the modification may need to be applied again depending on the installed Transformers version.

For reproducibility, keep the working dependency versions recorded in:

```
requirements.txt
```

---

## 🖥️ Streamlit Application

The frontend is developed using:

**Streamlit**

The application provides a simple interface for image upload, prediction, language selection, and management guidance.

### Main UI Features

#### 🌱 Project Information

The application displays the project title and purpose.

#### ℹ️ Supported Crops

The application provides important information about the supported crop categories and conditions.

#### 🌐 Language Selection

The user can choose:

- English
- Hindi (हिंदी)
- Gujarati (ગુજરાતી)

#### 📷 Image Upload

Supported formats:

- JPG
- JPEG
- PNG

#### 🔍 Disease Detection

The application displays:

- Crop
- Detected condition
- Confidence score
- Top predictions

#### 🌾 Management Guidance

The application displays the management and prevention guidance generated using the knowledge base and IBM Granite.

#### 👨‍💻 Sidebar Information

The Streamlit sidebar contains student and internship information.

It includes:

```
🌱 Crop Disease AI

Student
Name: Viren Vairagi

Internship
AI for Sustainability
Virtual Internship

Offered by 1M1B

In collaboration with AICTE

Co-certified by IBM SkillsBuild
```

---

## 🔄 Complete Application Workflow

```text
      USER
          │
          ▼
  Upload Leaf Image
          │
          ▼
 ┌──────────────────┐
 │  ViT Classifier  │
 └────────┬─────────┘
          │
          ▼
  Crop + Condition +
   Confidence Score
          │
          ▼
 ┌──────────────────┐
 │  Knowledge Base  │
 │  diseases.json   │
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐
 │ IBM Granite 4.1  │
 │      :3B         │
 └────────┬─────────┘
          │
          ▼
   English Guidance
          │
          ▼
  ┌──────────────────┐
  │   IndicTrans2    │
  │   Translation    │
  └────────┬─────────┘
           │
    ┌──────┼──────┐
    ▼      ▼      ▼
 English Hindi Gujarati
          हिंदी     ગુજરાતી
           │
           ▼
       Streamlit UI
```

---

## 📂 Project Structure

```
Crop_Disease_Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── predictor.py
│   ├── granite.py
│   ├── knowledge.py
│   └── translator.py
│
└── knowledge/
    └── diseases.json
```

---

## 📄 Project Files

### `app.py`

Main Streamlit application.

**Responsibilities:**

- Display the user interface
- Display supported crops
- Provide language selection
- Accept uploaded images
- Run disease prediction
- Display confidence
- Retrieve agricultural knowledge
- Call IBM Granite
- Translate the generated response
- Display the final guidance

### `src/predictor.py`

Responsible for loading and running the pretrained crop disease detection model.

**Model:** `wambugu71/crop_leaf_diseases_vit`

It also handles conversion of uploaded Streamlit files into compatible PIL images.

### `src/granite.py`

Responsible for interacting with IBM Granite 4.1:3B.

It receives the crop, detected condition, confidence, and relevant knowledge and generates structured guidance.

### `src/knowledge.py`

Responsible for loading and retrieving information from:

```
knowledge/diseases.json
```

### `src/translator.py`

Responsible for translating the generated English guidance into supported Indic languages using IndicTrans2.

### `knowledge/diseases.json`

Contains the structured agricultural information used to ground the generated guidance.

### `requirements.txt`

Contains the Python packages and versions required by the project.

```bash
pip install -r requirements.txt
```

### `.gitignore`

Prevents unnecessary or sensitive files from being uploaded to GitHub.

**Recommended contents:**

```
venv/
.venv/

__pycache__/
*.pyc

.env

.DS_Store

.ipynb_checkpoints/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Enter the project directory:

```bash
cd Crop_Disease_Prediction
```

### 2. Create a Virtual Environment

**macOS / Linux**

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

IBM Granite 4.1:3B is run locally using Ollama.

Install Ollama from:

[https://ollama.com/](https://ollama.com/)

Then download the Granite model:

```bash
ollama pull granite4.1:3b
```

Verify:

```bash
ollama list
```

You should see:

```
granite4.1:3b
```

You can test the model using:

```bash
ollama run granite4.1:3b
```

### 📦 Install the Python Ollama Package

If it is not already included in your environment:

```bash
pip install ollama
```

The Python application uses this package to communicate with the local Ollama service.

---

## ▶️ Run the Application

After installing the dependencies and downloading Granite:

```bash
streamlit run app.py
```

The application will normally be available at:

```
http://localhost:8501
```

Open the address in a browser.

---

## 🧪 Testing the Disease Detection Model

The pretrained disease model can also be tested independently.

**Example:**

```python
from transformers import pipeline

classifier = pipeline(
    "image-classification",
    model="wambugu71/crop_leaf_diseases_vit"
)

results = classifier(
    "path/to/leaf.jpg",
    top_k=5
)

for result in results:
    print(
        f"{result['label']}: "
        f"{result['score']:.2%}"
    )
```

---

## 📊 Example Prediction

Example output from the disease classifier:

```
Potato___Healthy          91.73%
Potato___Early_Blight      6.49%
Invalid                    1.02%
Corn___Common_Rust         0.24%
Corn___Healthy             0.18%
```

The application extracts the crop and condition from the prediction label.

For example:

```
Potato___Healthy
```

becomes:

- **Crop:** Potato
- **Condition:** Healthy

---

## 🌾 Example Application Result

### 🔍 Detection Result

- **Crop:** Potato
- **Status:** Healthy
- **Confidence:** 91.73%

The application can then generate:

### 🌾 Crop Management Guidance

- Diagnosis
- What it means
- What to do
- Prevention
- Important note

The final response can be displayed in English, Hindi, or Gujarati.

---

## 🛡️ Responsible AI Design

Agricultural AI applications can affect real-world decisions. Therefore, this project follows a cautious approach.

### 1. Knowledge-Grounded Generation

The language model receives information from the structured agricultural knowledge base.

This reduces the need for the LLM to independently invent agricultural recommendations.

### 2. Confidence Awareness

The application displays the disease classifier's confidence score.

If the confidence is low, the user is warned that the prediction should be verified.

### 3. No Unsupported Chemical Dosages

The application should not invent:

- Pesticide dosages
- Fertilizer dosages
- Chemical concentrations
- Treatment schedules

unless such information is explicitly available in the trusted source.

### 4. Expert Verification

Users should verify uncertain predictions with qualified agricultural professionals, particularly before making important treatment decisions.

---

## ⚠️ Limitations

### Disease Detection Limitations

The pretrained model may produce:

- False positives
- False negatives
- Incorrect predictions
- Lower confidence on unfamiliar images

Prediction performance may vary depending on:

- Image quality
- Lighting
- Leaf orientation
- Background
- Disease severity
- Crop variety
- Image characteristics

### Crop Coverage Limitations

The application is limited to the crop/condition classes supported by the loaded model.

It should not be assumed to detect all agricultural crops or diseases.

### Translation Limitations

Machine translation can sometimes produce:

- Incorrect wording
- Loss of technical meaning
- Inconsistent agricultural terminology

Important information should therefore be verified when accuracy is critical.

### Generative AI Limitations

IBM Granite can generate incorrect or incomplete responses if the provided knowledge is incomplete or inaccurate.

This is why the project uses a structured knowledge base as an information layer.

---

## 🔐 Security and API Key Guidelines

Never upload API keys, passwords, or other credentials to GitHub.

Do not commit:

```
.env
```

Use environment variables for secrets where required.

**Example:**

```
API_KEY=your_secret_key
```

Add `.env` to `.gitignore`.

---

## 🌍 AI for Sustainability

Agriculture is an important area for sustainability because crop health can influence productivity, food availability, and resource use.

This project demonstrates how AI can be applied to agriculture through:

- Computer vision
- Generative AI
- Knowledge-based information retrieval
- Multilingual translation
- User-friendly interfaces

**Potential benefits include:**

- Faster awareness of possible crop diseases
- Easier access to crop-health information
- Multilingual accessibility
- Support for students and agricultural learners
- Demonstration of AI-assisted sustainable agriculture

The project is intended as an educational and technological demonstration rather than a replacement for agricultural professionals.

---

## 💡 Why This Architecture?

The project uses separate components for separate responsibilities.

| Component              | Answers / Provides                                      |
|------------------------|---------------------------------------------------------|
| **Vision Transformer** | What condition does this leaf image most closely match? |
| **Knowledge Base**     | What trusted agricultural information is available about this condition? |
| **IBM Granite**        | How can this information be explained clearly to the user? |
| **IndicTrans2**        | How can the generated guidance be translated into the selected Indian language? |

This modular architecture makes it easier to improve individual components without redesigning the complete system.

---

## 🚀 Future Improvements

The current project can be extended in several ways.

### 1. Expand Crop Coverage

Add additional crops such as:

- Cotton
- Tomato
- Apple
- Grape
- Chili
- Soybean

### 2. Expand Disease Coverage

Add more disease categories by integrating a suitable trained or pretrained disease-classification model.

### 3. Improve the Agricultural Knowledge Base

The knowledge base can be expanded with information from reliable agricultural institutions and domain experts.

Possible additions:

- Symptoms
- Disease Causes
- Environmental Conditions
- Management
- Prevention
- Early Warning Signs

### 4. Improve Image Validation

Add a dedicated image-validation stage to determine whether:

- The uploaded image contains a leaf.
- The crop belongs to a supported category.
- The image quality is sufficient for prediction.

### 5. Improve Multilingual Support

Additional Indian languages could be supported in future versions.

Possible languages include:

- Marathi
- Bengali
- Tamil
- Telugu
- Kannada
- Malayalam
- Punjabi
- Odia

### 6. Cloud Deployment

The application can be deployed to a cloud platform so users can access it without setting up the complete environment locally.

A cloud architecture could separate:

```
Frontend
   ↓
Backend/API
   ↓
Disease Model
   ↓
Knowledge Base
   ↓
LLM
   ↓
Translation Service
```

### 7. Mobile Application

A future version could provide:

- Android Application
- iOS Application
- Progressive Web Application

Users could directly capture a crop-leaf image using their phone camera.

### 8. Offline AI

Future versions could investigate fully or partially offline operation.

Possible components:

```
Local Disease Model
+
Local Granite
+
Local Translation Model
```

This could be useful in areas with limited internet connectivity.

### 9. Expert Verification

An expert feedback system could be introduced where agricultural professionals can:

- Verify predictions
- Correct incorrect classifications
- Review generated guidance
- Provide feedback

This feedback could be used to improve future versions of the system.

### 10. Analytics

Future versions could include anonymous analytics such as:

- Most frequently detected crops
- Most common detected conditions
- Model confidence distribution
- Language usage

Such features should be implemented with appropriate privacy considerations.

---

## 🧪 Future Technical Enhancements

**Current**

```
Current
│
├── Pretrained ViT
├── JSON Knowledge Base
├── IBM Granite
├── IndicTrans2
└── Streamlit
```

**Future**

```
Advanced System
│
├── Improved Vision Model
├── Image Quality Validation
├── Larger Knowledge Base
├── RAG Pipeline
├── IBM Granite
├── Multilingual Translation
├── FastAPI Backend
├── Cloud Deployment
└── Mobile Application
```

---

## 🎓 Internship Information

**AI for Sustainability Virtual Internship**

This project was developed as part of the:

**AI for Sustainability Virtual Internship**

**Offered by**

1M1B

**In collaboration with**

AICTE

**Co-certified by**

IBM SkillsBuild

---

## 👨‍💻 Student Information

**Name:**  
Viren Vairagi

---

## Acknowledgements

This project uses open-source and pretrained technologies provided by different organizations and communities.

Special acknowledgement to:

- **Hugging Face**  
  For providing the Transformers ecosystem and access to pretrained machine-learning models.  
  Disease detection model: `wambugu71/crop_leaf_diseases_vit`

- **IBM**  
  For providing the Granite family of generative AI models.  
  This project uses: **IBM Granite 4.1:3B**

- **Ollama**  
  For providing a convenient way to run the Granite model locally.  
  [Ollama](https://ollama.com/)

- **AI4Bharat**  
  For providing IndicTrans2 models for Indian-language translation.  
  The project uses: `ai4bharat/indictrans2-en-indic-dist-200M`

- **Streamlit**  
  For providing the framework used to create the interactive web application.

- **Python Community**  
  For the Python ecosystem and open-source libraries used throughout the project.

---

## 📜 Disclaimer

This project is developed for educational, demonstration, and internship purposes.

The predictions produced by the AI model are not guaranteed to be accurate for every crop, disease, geographical region, crop variety, or image.

The management guidance generated by the application should not be considered a guaranteed cure or a replacement for professional agricultural advice.

Users should verify uncertain predictions with qualified agricultural experts before taking significant agricultural or chemical-treatment decisions.

---

## 📄 Third-Party Model and Software Licenses

This project uses third-party models, libraries, and software.

Before redistributing or deploying the project, review and comply with the applicable licenses and usage terms of:

- The pretrained crop disease model
- IBM Granite
- Ollama
- AI4Bharat IndicTrans2
- Hugging Face Transformers
- Streamlit
- Other dependencies listed in `requirements.txt`

The project repository should not imply ownership of third-party models or software.

---

## ⭐ Project Highlights

```
🌱 AI for Sustainable Agriculture

🔍 Crop Leaf Disease Detection
        ↓
🧠 Vision Transformer
        ↓
📚 Agricultural Knowledge Base
        ↓
🤖 IBM Granite 4.1:3B
        ↓
🌐 IndicTrans2 Translation
        ↓
🇬🇧 English
🇮🇳 Hindi (हिंदी)
🇮🇳 Gujarati (ગુજરાતી)
        ↓
🖥️ Streamlit Application
```

---

## 🌟 Conclusion

The **Crop Disease Detection & Management using AI** project demonstrates a modular AI system for agricultural sustainability.

Instead of relying on one model to perform every task, the project combines:

**Computer Vision + Knowledge Base + IBM Granite + Translation + Streamlit**

to create an application that can detect supported crop conditions and provide understandable multilingual management guidance.

The architecture can be expanded in the future with additional crops, diseases, languages, agricultural knowledge, expert feedback, cloud deployment, and mobile support.
