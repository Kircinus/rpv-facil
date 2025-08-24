from typing import List, Dict

def to_bank_payload(items: List[Dict]) -> Dict:
    # Mapeia itens de RPV para um payload de pagamento (mock)
    return {
        "lote": len(items),
        "total": sum([float(x.get("valor", 0)) for x in items]),
        "itens": items,
    }
