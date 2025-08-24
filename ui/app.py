import streamlit as st
import json, tempfile
from src.rpv_facil.workflow.pipeline import ingest_file, make_report

st.title("RPV Fácil — UI")
uploaded = st.file_uploader("Envie a intimação (PDF/XML)", type=["pdf","xml"])
if uploaded:
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded.name) as tmp:
        tmp.write(uploaded.getbuffer())
        data, status = ingest_file(tmp.name)
    st.success("Extraído!")
    st.json(data)
    if st.button("Gerar CSV"):
        out = make_report([data], "csv")
        with open(out, "rb") as f:
            st.download_button("Baixar CSV", f, file_name="rpvs.csv")
