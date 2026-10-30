# PRODIGY_GA_02 — Image Generation with Stable Diffusion

Task 2 of the Prodigy InfoTech Generative AI internship.

- Loads the Stable Diffusion v1.5 model through the Hugging Face Diffusers library.
- Turns a text prompt (`a futuristic cityscape with flying cars`) into an image.
- Shows the image and saves it as `futuristic_cityscape.png`. Uses the GPU when one is available.

**Tech:** Python · Hugging Face Diffusers · PyTorch

## Run

```bash
pip install diffusers transformers accelerate torch
python Task-2.py
```

The first run downloads the model (a few GB). Change the `prompt` string in `Task-2.py` to generate a different image.
