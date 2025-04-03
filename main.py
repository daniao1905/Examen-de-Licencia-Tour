
import streamlit as st
import json

# Cargar preguntas y respuestas
with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

with open("answers.json", "r", encoding="utf-8") as f:
    answers = json.load(f)

st.title("Examen de Selección - 総合旅行業務取扱管理者")

for qid in questions:
    pregunta = questions[qid]["pregunta"]
    opciones = questions[qid]["opciones"]

    st.subheader(f"Pregunta {qid}")
    st.write(pregunta)
    seleccion = st.radio("Selecciona una opción:", list(opciones.keys()), format_func=lambda x: f"{x}: {opciones[x]}", key=qid)

    if st.button(f"Verificar Respuesta {qid}"):
        correcta = answers[qid]["correcta"]
        razon = answers[qid]["razon"]
        if seleccion == correcta:
            st.success("¡Correcto!")
            st.info(f"Razón: {razon}")
        else:
            st.error(f"Incorrecto. La respuesta correcta es: {correcta}")
