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
    "Michele non è mai troppo lontano, anche quando è fisicamente lontano, il suo cuore è sempre vicino a te.",
        "Martina, ricorda che se la vita fosse un videogioco, tu saresti il personaggio principale con il potere di distruggere ogni livello!",
    "Martina, sei così brillante che se guardi troppo a lungo lo specchio, potrebbe scottarti!",
    "Martina, sei la versione umana di un unicorno che vola sopra l'arcobaleno. Nessuno è pronto per la tua magia!",
    "Se la fiducia fosse una superpotenza, Martina sarebbe Wonder Woman. E senza nemmeno bisogno di un mantello!",
    "Martina, il tuo sorriso è così potente che potrebbe risolvere la crisi energetica mondiale in un batter d'occhio.",
    "Non dimenticare mai, Martina, che sei un capolavoro in un mondo di bozzetti. La tua unicità è ciò che ti rende invincibile.",
    "Martina, la tua autostima è così alta che se ci mettessi una stella sopra, sarebbe un piccolo sole nel cielo!",
    "Scommetto che se Martina fosse una canzone, sarebbe un successo mondiale. Con un ritmo che non si dimentica mai!",
    "Martina, sei talmente incredibile che anche i supereroi si ispirano a te per essere più forti.",
    "Non solo Martina è forte, è anche la fonte di ispirazione per chiunque cerchi di diventare una versione migliore di sé!",
    "Martina, hai il tipo di bellezza che ti fa brillare anche nei giorni grigi. Sei come un raggio di sole in una giornata nuvolosa!",
    "Se la bellezza fosse una gara, Martina vincerebbe con un margine tale che gli altri partecipanti si metterebbero a fare i complimenti!",
    "Martina, non c'è nessun limite a ciò che puoi fare. Se lo sogni, lo realizzi. Sei una forza della natura!"
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
