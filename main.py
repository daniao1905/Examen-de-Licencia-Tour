import streamlit as st
import json
import re

st.set_page_config(page_title="R06 Examen", layout="centered")

def limpiar_opciones(texto):
    return set(re.findall(r"[ア-エ]", texto))

with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)
with open("answers.json", "r", encoding="utf-8") as f:
    answers = json.load(f)

st.title("Examen de Selección R06 - 国内旅行業務取扱管理者")

for qid in sorted(questions, key=lambda x: int(re.sub(r'[^0-9]', '', x))):
    pregunta = questions[qid]["pregunta"]
    opciones = questions[qid]["opciones"]
    correcta = limpiar_opciones(answers.get(qid, {}).get("correcta", ""))

    st.subheader(f"問{qid}")
    st.write(pregunta)

    seleccionadas = []
    for key, texto in opciones.items():
        if st.checkbox(f"{key}: {texto}", key=f"chk_{qid}_{key}"):
            seleccionadas.append(key)

    if st.button(f"確認 {qid}", key=f"btn_{qid}"):
        seleccionadas_set = set(seleccionadas)
        if seleccionadas_set == correcta:
            st.success("正解です！")
            st.info(answers.get(qid, {}).get("razon", ""))
        else:
            st.error("不正解。")
            st.info(f"正しい答えは: {'・'.join(sorted(correcta))}")