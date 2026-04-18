import streamlit as st
import random

if "x" not in st.session_state:
    st.session_state.x = random.randint(1, 20)
    st.session_state.tentatives = 0

st.title("🎮 Jeu de devinette")
st.write("Vous avez 3 tentatives")

numero = st.number_input("Choisissez un nombre entre 1 et 20", 1, 20)

if st.button("Valider"):
    st.session_state.tentatives += 1

    if numero == st.session_state.x:
        st.success("Bravo vous avez gagné ! 🎉")
        st.session_state.x = random.randint(1, 20)
        st.session_state.tentatives = 0

    elif st.session_state.tentatives < 3:
        if numero < st.session_state.x:
            st.warning("Plus grand")
        else:
            st.warning("Plus petit")

    else:
        st.error(f"Perdu ! Le nombre était {st.session_state.x}")
        st.session_state.x = random.randint(1, 20)
        st.session_state.tentatives = 0