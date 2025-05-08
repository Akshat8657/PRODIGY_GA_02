from diffusers import StableDiffusionPipeline
import torch

# Load the pre-trained Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# Use GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

# Define the text prompt
prompt = "a futuristic cityscape with flying cars"

# Generate the image
image = pipe(prompt).images[0]

# Show the image
image.show()

# Save the generated image
image.save("futuristic_cityscape.png")

print("Image saved as 'futuristic_cityscape.png'.")
