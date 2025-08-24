from lxml import etree

def parse_xml(path: str) -> dict:
    root = etree.parse(path).getroot()
    def get(tag):
        x = root.find(tag)
        return x.text.strip() if x is not None and x.text else None
    return {
        "processo": get("Processo"),
        "exequente": get("Exequente"),
        "cpf": get("CPF"),
        "valor": get("Valor"),
        "vara": get("Vara"),
        "data": get("Data"),
        "banco": get("Banco"),
        "agencia": get("Agencia"),
        "conta": get("Conta"),
    }
