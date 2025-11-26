from pathlib import Path
from PIL import Image

base = Path('C:/datasets')
paths = [
    base / 'both_deepfake' / 'real' / 'frames',
    base / 'both_deepfake' / 'fake' / 'frames',
    base / 'base_deepfake' / 'val' / 'real' / 'frames',
    base / 'base_deepfake' / 'val' / 'fake' / 'frames',
    base / 'augment_deepfake' / 'val' / 'real' / 'frames',
    base / 'augment_deepfake' / 'val' / 'fake' / 'frames',
    base / 'precomputed'
]

for p in paths:
    p.mkdir(parents=True, exist_ok=True)

# create one dummy image in each frames directory
for p in paths:
    if p.name == 'frames':
        img_path = p / 'img1.png'
        if not img_path.exists():
            Image.new('RGB', (64, 64), (128, 128, 128)).save(img_path)

print('Created dataset folders and dummy images under C:/datasets')
