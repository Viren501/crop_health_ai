import streamlit as st


from src.predictor import predict
from src.knowledge import get_disease_knowledge
from src.granite import generate_guidance
from src.translator import translate_to_indic


st.set_page_config(
    page_title="Crop Health AI",
    page_icon="🌱",
    layout="wide"
)


# ============================================================
# SUPPORTED CROPS & DISEASES
# ============================================================

SUPPORTED_CROPS = {
    "Corn": [
        "Common Rust",
        "Gray Leaf Spot",
        "Leaf Blight",
        "Healthy"
    ],
    "Potato": [
        "Early Blight",
        "Late Blight",
        "Healthy"
    ],
    "Rice": [
        "Brown Spot",
        "Leaf Blast",
        "Healthy"
    ],
    "Wheat": [
        "Brown Rust",
        "Yellow Rust",
        "Healthy"
    ]
}


# ============================================================
# TITLE
# ============================================================

st.title(
    "🌱 Crop Disease Detection & Management"
)


st.write(
    "Upload a crop leaf image to detect "
    "supported diseases and receive "
    "management guidance."
)


# ============================================================
# IMPORTANT INFORMATION
# ============================================================

with st.expander("ℹ️ Important Information — Supported Crops & Diseases", expanded=True):

    st.write(
        "This AI model is currently designed for **4 types of crops** "
        "and their supported diseases/healthy conditions."
    )

    st.write("### 🌾 Supported Crops")

    for crop, diseases in SUPPORTED_CROPS.items():
        st.markdown(
            f"**{crop}** — {len(diseases)} conditions: "
            + ", ".join(diseases)
        )

    st.divider()

    total_classes = sum(len(diseases) for diseases in SUPPORTED_CROPS.values())

    st.write(f"**Number of supported crops:** {len(SUPPORTED_CROPS)}")
    st.write(f"**Number of crop conditions:** {total_classes}")

    st.info(
        "📌 For the best results, upload a clear image of a leaf "
        "from one of the supported crops above."
    )



# ============================================================
# Language
# ============================================================

language = st.selectbox(
    "Select language",
    [
        "English",
        "Hindi (हिंदी)",
        "Gujarati (ગુજરાતી)"
    ]
)


# ============================================================
# Upload
# ============================================================

uploaded_file = st.file_uploader(
    "Upload a crop leaf image",
    type=[
        "jpg",
        "jpeg",
        "png"
    ]
)


if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded leaf",
        use_container_width=True
    )


    if st.button("Analyze Leaf"):

        # ====================================================
        # 1. ViT prediction
        # ====================================================

        with st.spinner(
            "Detecting crop condition..."
        ):

            results = predict(
                uploaded_file,
                top_k=3
            )


        top_result = results[0]


        label = top_result["label"]
        confidence = top_result["score"]


        # ====================================================
        # 2. Invalid image
        # ====================================================

        if label == "Invalid":

            st.error(
                "The model could not identify "
                "a supported crop leaf."
            )


            st.info(
                "Please upload a clear image of a "
                "corn, potato, rice, or wheat leaf."
            )


            st.stop()


        # ====================================================
        # 3. Parse label
        # ====================================================

        if "___" in label:

            crop, disease = label.split(
                "___",
                1
            )

        else:

            crop = "Unknown"
            disease = label


        # ====================================================
        # 4. Detection result
        # ====================================================

        st.subheader(
            "🔍 Detection Result"
        )


        st.write(
            f"**Crop:** {crop}"
        )


        if disease == "Healthy":

            st.success(
                "🌿 Status: Healthy"
            )

        else:

            st.warning(
                f"⚠️ Detected condition: {disease}"
            )


        st.write(
            f"**Confidence:** "
            f"{confidence:.2%}"
        )


        # ====================================================
        # 5. Top predictions
        # ====================================================

        with st.expander(
            "View top predictions"
        ):

            for result in results:

                st.write(
                    f"{result['label']}: "
                    f"{result['score']:.2%}"
                )


        # ====================================================
        # 6. Confidence warning
        # ====================================================

        if confidence < 0.60:

            st.warning(
                "The model confidence is relatively low. "
                "Please verify the result using a clearer "
                "image or consult an agricultural expert."
            )


        # ====================================================
        # 7. Knowledge Base
        # ====================================================

        disease_knowledge = (
            get_disease_knowledge(label)
        )


        if not disease_knowledge:

            st.error(
                "Management information for this "
                "prediction is not available yet."
            )

            st.stop()


        # ====================================================
        # 8. Granite
        # ====================================================

        with st.spinner(
            "Generating management guidance with IBM Granite..."
        ):

            english_guidance = generate_guidance(
                crop=crop,
                disease=disease,
                confidence=confidence,
                knowledge=disease_knowledge
            )


        # ====================================================
        # 9. Translation
        # ====================================================

        if language == "English":
            final_guidance = english_guidance

        elif language == "Hindi (हिंदी)":
            final_guidance = translate_to_indic(
                english_guidance,
                "Hindi"
            )

        elif language == "Gujarati (ગુજરાતી)":
            final_guidance = translate_to_indic(
                english_guidance,
                "Gujarati"
            )


        # ====================================================
        # 10. Final result
        # ====================================================

        st.subheader(
            "🌾 Crop Management Guidance"
        )


        st.markdown(
            final_guidance
        )


        # ====================================================
        # 11. Technical information
        # ====================================================

        with st.expander(
            "Technical information"
        ):

            st.write(
                "Disease detection model:"
            )

            st.code(
                "wambugu71/crop_leaf_diseases_vit"
            )


            st.write(
                "Language model:"
            )

            st.code(
                "IBM Granite 4.1:3B"
            )


            st.write(
                "Translation model:"
            )

            st.code(
                "AI4Bharat IndicTrans2 "
                "en-indic-dist-200M"
            )

# ============================================================
# SIDEBAR — STUDENT & INTERNSHIP INFORMATION
# ============================================================

with st.sidebar:

    st.title("🌱 Crop Disease AI")

    st.divider()

    st.subheader("👨‍💻 Student")

    st.markdown("""
    **Name:**  
    Viren Vairagi

    """)

    st.divider()

    st.subheader("🎓 Internship")

    st.markdown("""
    **AI for Sustainability**  
    **Virtual Internship**

    Offered by **1M1B**

    In collaboration with **AICTE**

    Co-certified by  
    **IBM SkillsBuild**
    """)

    st.divider()

    st.caption(
        "🌍 AI for Sustainability\n\n"
        "Crop Disease Detection & Management"
    )