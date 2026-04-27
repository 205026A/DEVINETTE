import streamlit as st
import random

if "x" not in st.session_state:
    st.session_state.x = random.randint(1, 20)
    st.session_state.tentatives = 0
    st.session_state.gagne=False
    st.session_state.perdu = False

st.title("🎮 Jeu de devinette")
st.write("Vous avez 3 tentatives")
st.write(f"Tentatives restantes : {max(0, 3 - st.session_state.tentatives)}")
st.progress(min(1.0, st.session_state.tentatives / 3))

numero = st.number_input("Choisissez un nombre entre 1 et 20", 1, 20)

if st.button("Valider") and not st.session_state.gagne and st.session_state.tentatives < 3:
    st.session_state.tentatives += 1

    if numero == st.session_state.x:
        st.success("Bravo vous avez gagné ! 🎉")
        st.session_state.gagne=True

    elif st.session_state.tentatives < 3:
        if numero < st.session_state.x:
            st.warning("Plus grand")
        else:
            st.warning("Plus petit")

    else:
        st.error(f"Perdu ! Le nombre était {st.session_state.x}")
        st.session_state.perdu = True
if st.button("Rejouer"):
    st.session_state.x = random.randint(1, 20)
    st.session_state.tentatives = 0
    st.session_state.gagne = False
if st.session_state.gagne or st.session_state.perdu:
    st.info("Cliquez sur Rejouer pour recommencer")
