import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)


MODEL_NAME = (
    "ai4bharat/indictrans2-en-indic-dist-200M"
)


LANGUAGE_CODES = {
    "Hindi": "hin_Deva",
    "Gujarati": "guj_Gujr"
}


_tokenizer = None
_model = None


def load_translator():

    global _tokenizer
    global _model


    if _tokenizer is not None:
        return


    _tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )


    _model = AutoModelForSeq2SeqLM.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )


    device = (
        "mps"
        if torch.backends.mps.is_available()
        else "cpu"
    )


    _model = _model.to(device)


def translate_to_indic(
    text,
    language
):

    if language == "English":
        return text


    if language not in LANGUAGE_CODES:
        raise ValueError(
            f"Unsupported language: {language}"
        )


    load_translator()


    device = next(
        _model.parameters()
    ).device


    target_language = LANGUAGE_CODES[
        language
    ]


    formatted_text = (
        f"eng_Latn {target_language} {text}"
    )


    inputs = _tokenizer(
        formatted_text,
        return_tensors="pt",
        padding=True
    )


    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }


    with torch.no_grad():

        generated_tokens = _model.generate(
            **inputs,
            max_length=512,
            num_beams=5,
            num_return_sequences=1
        )


    translated_text = _tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True
    )[0]


    return translated_text
