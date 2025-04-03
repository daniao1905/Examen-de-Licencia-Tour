
import streamlit as st
import json

st.set_page_config(page_title="Examen 総合旅行業務", layout="centered")

# Cargar preguntas y respuestas
with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

with open("answers.json", "r", encoding="utf-8") as f:
    answers = json.load(f)

st.title("Examen de Selección - 総合旅行業務取扱管理者")

for qid in sorted(questions, key=lambda x: int(x)):
    pregunta = questions[qid]["pregunta"]
    opciones = questions[qid]["opciones"]

    st.subheader(f"{pregunta}")
    seleccion = st.radio(
        "選択肢を選んでください:",
        options=[(k, f"{k}: {v}") for k, v in opciones.items()],
        format_func=lambda x: x[1],
        key=qid
    )
    seleccion = seleccion[0]

    if st.button(f"確認 {qid}", key=f"check_{qid}"):
        correcta = answers.get(qid, {}).get("correcta", "")
        razon = answers.get(qid, {}).get("razon", "")
        if seleccion == correcta:
            st.success("正解です！")
            st.info(f"理由: {razon}")
        else:
            st.error(f"不正解。正しい答えは {correcta} です。")
