from pathlib import Path
from typing import Tuple, Dict, Any, List
import json
import pandas as pd
from ..models import RPV
from ..extractor.pdf_extractor import extract_text, guess_fields
from ..extractor.xml_extractor import parse_xml
from ..extractor.normalizer import normalize_payload

OUT_DIR = Path("data/out")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def ingest_file(path: str) -> Tuple[Dict[str, Any], str]:
    p = Path(path)
    if p.suffix.lower() == ".xml":
        raw = parse_xml(str(p))
    else:
        text = extract_text(str(p))
        raw = guess_fields(text)
    payload = normalize_payload(raw)
    model = RPV.model_validate(payload)
    return model.model_dump(by_alias=True), "ok"

def make_report(items: List[dict], fmt: str = "csv") -> str:
    df = pd.DataFrame(items)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if fmt == "xlsx":
        out = OUT_DIR / "rpvs.xlsx"
        df.to_excel(out, index=False)
    else:
        out = OUT_DIR / "rpvs.csv"
        df.to_csv(out, index=False)
    return str(out)
