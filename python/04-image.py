import os
from openai import OpenAI
import base64

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# 画像ファイルをbase64エンコード
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

#base64_image = encode_image("./data/photo.jpg")  # 画像ファイル
base64_image = encode_image("./data/atcoder.jpg")  # 画像ファイル

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a skilled engineer."},
        #{"role": "system", "content": "You are an animal doctor in Scotland."},
        {"role": "user", "content": [
            #{"type": "text", "text": "What's the animal in the photo?"},
            {"type": "text", "text": "Show Python program for the problem attached in the image."},
            {"type": "image_url", "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"}
            }
        ]}
    ],
    temperature=0.0,
)

print(response.choices[0].message.content)
