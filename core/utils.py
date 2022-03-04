import yaml
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

def loadyaml(filename= BASE_DIR / 'translations.yaml'):
    try:
        file = open(filename)
        loaded = yaml.safe_load(file)
        file.close()
        return loaded
    except FileNotFoundError:
        raise FileNotFoundError(f'Specified wrong file name: \'{filename}\'')

def parse_term(term: str) -> str:
    return term.lower()