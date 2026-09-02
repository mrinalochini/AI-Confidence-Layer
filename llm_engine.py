# Confidence-app
import streamlit as st
import json
from openai import OpenAI

st.title("AI Confidence Layer Prototype")
st.write("Test out how an AI distinguishes between verified facts, logical guesses, and speculation.")

# Fetch the key securely from Streamlit Secrets
api_key = st.secrets["GROQ_API_KEY"]

user_question = st.text_input("Ask a question based on your document or topic:")

if st.button("Generate Answer"):
    if not user_question:
        st.warning("Please type a question.")
    else:
        client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
        
        with st.spinner("Analyzing and confidence-scoring response..."):
            prompt = f"""
    You are the AI answer-generation component of an AI Confidence Layer.

    Answer the user's question clearly and concisely.

    Break the answer into individual factual claims.

    Rules:
    1. Each claim must contain one main factual assertion.
    2. Do not combine multiple independent facts into one claim.
    3. Do not assign confidence labels.
    4. Do not use words such as GROUNDED, INFERRED, or SPECULATIVE.
    5. Return ONLY valid JSON.

    Use exactly this format:
    
    {{
        "question": "{user_question}",
        "claims": [
            {{
                "id": 1,
                "text": "First factual claim."
            }},
            {{
                "id": 2,
                "text": "Second factual claim."
            }}
        ]
    }}
    
    User question:
    {user_question}
    """
    response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": prompt}],
    response_format={"type": "json_object"},
    stream=False
    )
            
            answer_text = response.choices[0].message.content
            result = json.loads(answer_text)
            
            st.subheader("Confidence-Layered Output:")
            for claim in result["claims"]:

                st.markdown(
                    f"""
                    **Claim {claim['id']}**

                    {claim['text']}
                    """
                )
