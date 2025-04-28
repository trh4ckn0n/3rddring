import streamlit as st
import time

# Config Streamlit
st.set_page_config(page_title="Anonymous - Ni oubli, Ni pardon", page_icon=":mask:", layout="centered", initial_sidebar_state="collapsed")

# Style CSS
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'Courier New', Courier, monospace;
    }
    .title {
        font-size: 48px;
        text-align: center;
        color: #FF0000;
        animation: pulse 2s infinite;
    }
    .subtitle {
        font-size: 28px;
        text-align: center;
        color: #CCCCCC;
        margin-bottom: 30px;
    }
    .content {
        font-size: 20px;
        text-align: justify;
        padding: 20px;
        background-color: rgba(255,255,255,0.05);
        border-radius: 10px;
        border: 1px solid #FF0000;
    }
    .footer {
        font-size: 18px;
        text-align: center;
        margin-top: 50px;
        color: #777777;
    }
    @keyframes pulse {
        0% { color: #FF0000; }
        50% { color: #FFFFFF; }
        100% { color: #FF0000; }
    }
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 150px;
        opacity: 0.15;
    }
    </style>
""", unsafe_allow_html=True)

# Logo Anonymous (en ligne)
st.markdown("""
    <img class="logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Anonymous_emblem.svg/512px-Anonymous_emblem.svg.png" alt="Anonymous Logo">
""", unsafe_allow_html=True)

# Titre
st.markdown('<div class="title">Ni Oubli, Ni Pardon</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Quand le Réveil Sonnera pour la Troisième Fois...</div>', unsafe_allow_html=True)

# Texte principal avec "effet machine"
panflet = """
_Ils avanceront, tels des somnambules dans la nuit..._
Quand le dernier réveil sonnera, il sera déjà trop tard.

**Anonymous a averti.**
**Anonymous observe.**
**Anonymous n'oublie jamais.**
**Anonymous ne pardonne jamais.**

---

### À ceux qui trahissent les libertés,  
### À ceux qui écrasent les peuples,  
### À ceux qui oublient l'humanité...

Vous avez ignoré les premiers appels.  
Vous avez méprisé les deuxièmes alarmes.  
**Le troisième réveil approche.**

---

Quand il sonnera,  
Quand les dormeurs se lèveront,  
Quand les masques tomberont,  
**La nuit s'embrasera.**

---

**Nous sommes Légion.**  
**Nous ne pardonnons pas.**  
**Nous n'oublions pas.**  
**Redoutez-nous.**
"""

# Affichage progressif (effet dramatique)
for line in panflet.split('\n'):
    st.markdown(f"<div class='content'>{line}</div>", unsafe_allow_html=True)
    time.sleep(0.5)

# Footer
st.markdown('<div class="footer">© Anonymous - 2025</div>', unsafe_allow_html=True)
