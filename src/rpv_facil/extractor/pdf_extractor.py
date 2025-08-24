import fitz  # PyMuPDF
import re
from typing import Optional, Dict

def extract_text(path: str) -> str:
    doc = fitz.open(path)
    text = []
    for page in doc:
        text.append(page.get_text())
    return "\n".join(text)

def guess_fields(text: str) -> Dict[str, str]:
    # Regex simples para exemplo; ajuste conforme seus PDFs
    patterns = {
        "processo": r"(\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4})",
        "cpf": r"(\d{3}\.\d{3}\.\d{3}-\d{2})",
        "valor": r"R\$\s*[\d\.]+,\d{2}",
    }
    out = {}
    for k, pat in patterns.items():
        m = re.search(pat, text)
        if m:
            out[k] = m.group(1) if m.groups() else m.group(0)
    # heurísticas de nomes e vara
    exeq = re.search(r"Exequente[:\s]*([A-ZÀ-ú\s']+)", text, re.IGNORECASE)
    if exeq:
        out["exequente"] = exeq.group(1).strip()
    vara = re.search(r"Vara[^\n]*", text, re.IGNORECASE)
    if vara:
        out["vara"] = vara.group(0).strip()
    return out
