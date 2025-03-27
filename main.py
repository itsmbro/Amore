import streamlit as st
import random

# Lista di frasi rassicuranti e divertenti
frasi = [
    "Michele non vuole andarsene, ti ama e lo sai.",
    "Anche se Michele venerdì va dai suoi amici, questo non significa che non ti voglia più.",
    "Michele sta solo cercando di sembrare misterioso, ma in realtà non vede l'ora di passare del tempo con te.",
    "Michele è solo preso da mille cose, ma quando ti guarda, si dimentica di tutto.",
    "Non preoccuparti, Michele sta solo cercando di capire se la pizza è più importante di te... ma sappiamo tutti come finirà!",
    "Michele ti ama più di quanto ami le sue scarpe nuove. E questo è dire tanto.",
    "Michele ti pensa sempre, anche quando sembra che stia guardando il muro. È il muro dell'amore!",
    "Quando Michele dice che ha bisogno di tempo, intende 'tempo per pensare a come sorprenderti'.",
    "Non preoccuparti, Michele è solo in modalità 'uomo misterioso', ma tra poco tornerà a svelare tutti i suoi sentimenti.",
    "Michele potrebbe sembrare distratto, ma ti sta pensando, solo che sta cercando di trovare il miglior modo per dirtelo senza sembrare troppo tenero.",
    "Michele non è mai troppo lontano, anche quando è fisicamente lontano, il suo cuore è sempre vicino a te."
]

# Funzione per generare una frase casuale
def genera_frase():
    return random.choice(frasi)

# Configura l'interfaccia Streamlit
st.title("Frasi Rassicuranti e Divertenti per Michele 🥰")
st.write("Clicca sul bottone per ottenere una frase rassicurante e divertente da Michele!")

# Bottone per generare la frase
if st.button("Genera una frase"):
    frase = genera_frase()
    st.subheader(frase)
