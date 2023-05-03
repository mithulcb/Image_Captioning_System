from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image

model1 = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor1 = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer1 = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device1 = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model1.to(device1)


def predict_step(new_captions,image_paths,diversity,penalty,temp,topp,topk):
  gen_kwargs = {"max_length": 16, "num_beams": 4, "num_beam_groups":2, "diversity_penalty":diversity,"penalty_alpha":penalty,"temperature":temp,"top_p":topp,"top_k":topk}
  images = []
  for image_path in image_paths:
    i_image = Image.open(image_path)
    if i_image.mode != "RGB":
      i_image = i_image.convert(mode="RGB")

    images.append(i_image)

  pixel_values = feature_extractor1(images=images, return_tensors="pt").pixel_values
  pixel_values = pixel_values.to(device1)
  

  output_ids = model1.generate(pixel_values, **gen_kwargs)

  preds = tokenizer1.batch_decode(output_ids, skip_special_tokens=True)
  preds = [pred.strip() for pred in preds]
  new_captions.append(preds)
  return new_captions