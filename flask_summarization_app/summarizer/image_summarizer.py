from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import io

# Load the image summarization model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def summarize_image(image_file):
    image = Image.open(io.BytesIO(image_file.read()))
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)
