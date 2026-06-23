import streamlit as st
from openai import OpenAI
from PIL import Image
import base64
import io
from dotenv import load_doenv 

# Create OpenAI client

api=loadenv.("../../.env.local")
client = OpenAI(api_key=api)

st.title("Image Text Detector")

# Upload image
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    # Show image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert image to base64
    image_bytes = uploaded_file.read()
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    st.write("Checking image for text...")

    # Send image to OpenAI
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Does this image contain any text? If yes, extract all text."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ]
    )

    # Get AI response
    result = response.choices[0].message.content

    st.subheader("OpenAI Response")
    st.write(result)