import streamlit as st
from pdf_reader import extract_text
from summarizer import generate_summary

st.set_page_config(
    page_title="Research Paper Summarizer",
    page_icon="📄"
)

st.title(
    "📄 Research Paper Summarizer"
)

uploaded_file = st.file_uploader(
    "Upload Research Paper",
    type="pdf"
)

if uploaded_file:

    text = extract_text(
        uploaded_file
    )

    st.success(
        "Research paper uploaded successfully."
    )

    st.subheader(
        "Extracted Text"
    )

    st.text_area(
        "Paper Content",
        text[:3000],
        height=300
    )

    if st.button(
        "Generate Summary"
    ):

        with st.spinner(
            "Generating Summary..."
        ):

            summary = generate_summary(
                text
            )

            st.subheader(
                "Summary"
            )

            st.write(
                summary
            )

            st.download_button(
                "Download Summary",
                summary,
                file_name="summary.txt"
            )