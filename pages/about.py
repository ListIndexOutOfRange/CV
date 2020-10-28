import streamlit as st

def content():
    st.title('About me')
    st.write(
        "I'm a 24 french engineering student at __IMT Atlantique__, one of the top french _grandes écoles_.    \n"
        "During my studies, I specialised in __deep learning__, especially __computer vision__ and its  \
        applications in __healthcare__ and __radiology__.    \n"
        "I'm also very interested in everything related to __efficient implementations__ of deep learning \
        (quantization, pruning, knowledge distillation,  ...).    \n"
        "My main skills include python development in general, more specifically Pytorch and its ecosystem. \
        (I'm a huge fan of [Pytorch Lightning](https://www.pytorchlightning.ai/) to be even more specific).")
    st.write("You can find my github [here](https://github.com/the-dharma-bum)")