import requests
from PIL import Image
from io import BytesIO
from gtts import gTTS
from moviepy.editor import *
import os

# ========== CONFIGURATION ==========
HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL_ENDPOINT = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"  # or your AnimalDiff model

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}
# ===================================

def generate_image(prompt: str, output_path="scene.png"):
    payload = {"inputs": prompt}
    response = requests.post(HF_MODEL_ENDPOINT, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"HuggingFace API error: {response.status_code}, {response.text}")
    
    image = Image.open(BytesIO(response.content))
    image.save(output_path)
    return output_path

def generate_voice(text: str, output_path="voice.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)
    return output_path

def create_animated_video(image_path: str, audio_path: str, output_path="final_output.mp4"):
    audio = AudioFileClip(audio_path)
    img_clip = ImageClip(image_path).set_duration(audio.duration).set_audio(audio)

    # Optional pan-zoom effect
    animated = img_clip.fx(vfx.zoom_in, factor=1.1)

    animated.write_videofile(output_path, fps=24)
    return output_path

# === EXAMPLE PROMPT ===
prompt = "A cartoon panda playing a guitar under a rainbow"

# === RUN PIPELINE ===
print("Generating image from Hugging Face...")
image_file = generate_image(prompt)

print("Generating voice from text...")
audio_file = generate_voice(prompt)

print("Creating animated video...")
final_video = create_animated_video(image_file, audio_file)

print(f"✅ Done! Final video saved as: {final_video}")
