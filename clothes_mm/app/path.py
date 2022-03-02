from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_DIR = os.path.join(BASE_DIR, 'media')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

TEMP_DIR = os.path.join(MEDIA_DIR, 'temp')

DETECT_NAME = ''
