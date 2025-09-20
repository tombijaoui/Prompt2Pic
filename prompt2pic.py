import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Prompt2Pic", page_icon="🖼️", layout="wide")

def logo_b64(path="prompt2pic_logo.png"):
    p = Path(path)
    if not p.exists():
        return None
    return base64.b64encode(p.read_bytes()).decode("utf-8")

b64 = logo_b64()

st.markdown(
    f"""
    <div style="display:flex; align-items:center; justify-content:center; gap:12px; margin-bottom:10px;">
        <img src="data:image/png;base64,{b64}" width="48" height="48" style="border-radius:8px;" />
        <span style="font-size: 2.5rem;
                     font-weight: 700;
                     background: linear-gradient(90deg, #6EE7F9, #A78BFA, #F472B6);
                     -webkit-background-clip: text;
                     background-clip: text;
                     color: transparent;">
            Prompt2Pic
        </span>
    </div>
    """,
    unsafe_allow_html=True,)

st.caption("Describe the image you're looking for. We'll plug retrieval next.")
st.divider()

# --- Main
st.subheader("Your query")
query = st.text_input(
    label="",
    placeholder="e.g., an orange cat napping on a sunny couch",
)

col_run, col_info = st.columns([1, 4])
with col_run:
    save_clicked = st.button("Save query", type="primary", use_container_width=True)
with col_info:
    st.caption("For now we only save the query. Retrieval comes next.")

st.divider()

if save_clicked:
    if query.strip():
        st.success(f"Saved query: **{query}**")
        st.session_state["last_query"] = query.strip()
    else:
        st.warning("Please enter a query before saving.")

st.caption("MVP interface — next step: FAISS + embeddings")
