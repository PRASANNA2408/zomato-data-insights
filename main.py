import streamlit as st

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

        .centered {
            display: flex;
            flex-direction: column;
            align-items: center;
            font-family: "Lucida Console", "Courier New", monospace;
            margin-top: 100px;
        }

        h1 {
            font-size: 6em;
            font-weight: 500;
            margin: 0;
        }

        h3 {
            font-size: 1.5em;
            font-weight: 400;
            margin: 0;
        }
    </style>

    <div class="centered">
        <h1>Welcome</h1>
        <h3>to the</h3>
        <h3>Zomato Data Insights !!</h3>
    </div>
""", unsafe_allow_html=True)

# Attractive image below the welcome text
st.image("https://images.unsplash.com/photo-1504674900247-0877df9cc836", use_column_width=True, caption="Deliciously Data-Driven 🍽️")
