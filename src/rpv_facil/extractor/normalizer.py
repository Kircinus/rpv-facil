from datetime import datetime
from typing import Dict, Any

def normalize_payload(d: Dict[str, Any]) -> Dict[str, Any]:
    # normaliza chaves comuns
    out = dict(d)
    # data -> ISO
    dt = out.get("data")
    if dt and isinstance(dt, str):
        try:
            out["data"] = datetime.fromisoformat(dt).date().isoformat()
        except Exception:
            pass
    # valor -> como string normalizada
    if "valor" in out and isinstance(out["valor"], str):
        s = out["valor"].replace("R$", "").replace(".", "").replace(" ", "").replace("\u00A0","")
        out["valor"] = s.replace(",", ".")
    return out
