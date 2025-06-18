import torch
from torchvision import models, transforms
from PIL import Image
import io

# Pretrained ResNet for demo — you can load your own TorchScript model here
model = models.resnet18(pretrained=True)
model.eval()

LABELS = ['t-shirt', 'jeans', 'jacket',  'shirt', 'skirt']

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict_image(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(tensor)
        predicted_idx = torch.argmax(outputs, dim=1).item()

    return LABELS[predicted_idx % len(LABELS)]  # Dummy map

