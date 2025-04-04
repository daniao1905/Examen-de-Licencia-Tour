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
    correcta = set(answers.get(qid, {}).get("correcta", ""))

    st.subheader(f"問{qid}")
    st.write(pregunta)

    checks = {}
    cols = st.columns(len(opciones))
    for i, (key, texto) in enumerate(opciones.items()):
        with cols[i]:
            checks[key] = st.checkbox(f"{key}: {texto}", key=f"chk_{qid}_{key}")

    if st.button(f"確認 {qid}", key=f"btn_{qid}"):
        seleccionadas = set(k for k, v in checks.items() if v)
        if seleccionadas == correcta:
            st.success("正解です！")
            st.info(answers.get(qid, {}).get("razon", ""))
        else:
            st.error(f"不正解。正しい答えは {'・'.join(correcta)} です。")