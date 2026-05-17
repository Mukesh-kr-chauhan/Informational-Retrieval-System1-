import os
from pathlib import path
import logging

logging.basicConfig(level=logging.INFO)

logging.basicConfig(Level=logging.INFO,format='[%(asctime)s]: %(message)s:')

list_of_files =[
    f"src/__init__.py",
    f"src/helper.py",
    ".env",
    "requirement.text",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
]