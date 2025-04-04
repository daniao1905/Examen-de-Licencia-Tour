import streamlit as st
import json

st.set_page_config(page_title="R06 Examen", layout="centered")

with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

with open("answers.json", "r", encoding="utf-8") as f:
    answers = json.load(f)

st.title("Examen de Selección R06 - 国内旅行業務取扱管理者")

for qid in sorted(questions, key=lambda x: int(x)):
    pregunta = questions[qid]["pregunta"]
    opciones = questions[qid]["opciones"]
    correcta = answers.get(qid, {}).get("correcta", "")

    st.subheader(f"問{qid}")
    st.write(pregunta)

    seleccion = st.multiselect(
        "選択肢を選んでください:",
        options=[(k, f"{k}: {v}") for k, v in opciones.items()],
        format_func=lambda x: x[1],
        key=f"sel_{qid}"
    )
    seleccion_keys = [s[0] for s in seleccion]

    if st.button(f"確認 {qid}", key=f"btn_{qid}"):
        if set(seleccion_keys) == set(correcta):
            st.success("正解です！")
            st.info(f"理由: {answers.get(qid, {}).get('razon', '')}")
        else:
            st.error(f"不正解。正しい答えは {correcta} です。")