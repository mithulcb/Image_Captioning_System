import open_clip
from PIL import Image
import torch

model, _, transform = open_clip.create_model_and_transforms(
  model_name="coca_ViT-L-14",
  pretrained="mscoco_finetuned_laion2B-s13B-b90k"
)


def c(new_captions,path_names):
    
    im = Image.open(path_names).convert("RGB")
    im = transform(im).unsqueeze(0)
    with torch.no_grad(), torch.cuda.amp.autocast(): 
        generated = model.generate(im)
    caption = open_clip.decode(generated[0])
    caption = caption.replace("<start_of_text>", "").replace("<end_of_text>", "").strip()
    new_captions.append(caption)
    return new_captions