import ollama


MODEL_NAME = "granite4.1:3b"


def generate_guidance(
    crop,
    disease,
    confidence,
    knowledge
):

    prompt = f"""
You are an agricultural crop-health assistant.

A computer vision model analyzed a crop leaf.

Crop:
{crop}

Detected condition:
{disease}

Model confidence:
{confidence:.2%}

Use the trusted agricultural information below.

Trusted information:
{knowledge}

Your task is to explain the information clearly.

Do NOT:
- invent pesticide names
- invent chemical dosages
- invent fertilizer dosages
- claim that the disease is certainly cured
- provide unsupported medical or agricultural claims

If confidence is low, tell the user that the result
should be verified by an agricultural expert.

If the crop is healthy, provide general crop-health
and prevention advice instead of disease treatment.

Return the response in English using exactly these sections:

## Diagnosis

## What it means

## What to do

## Prevention

## Important note

Keep the response practical and easy to understand.
"""


    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.2
        }
    )


    return response["message"]["content"]
