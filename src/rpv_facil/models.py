from pydantic import BaseModel, Field, validator
from datetime import date
from typing import Optional

class RPV(BaseModel):
    processo: str = Field(..., description="Número do processo")
    exequente: str
    cpf_cnpj: str = Field(..., alias="cpf")
    valor: float
    vara: Optional[str] = None
    data: Optional[date] = None
    banco: Optional[str] = None
    agencia: Optional[str] = None
    conta: Optional[str] = None

    @validator("valor", pre=True)
    def parse_valor(cls, v):
        if isinstance(v, (int, float)):
            return float(v)
        s = str(v)
        s = s.replace("R$", "").replace(".", "").replace(" ", "").replace(" ","")
        s = s.replace(",", ".")
        try:
            return float(s)
        except Exception:
            raise ValueError("Valor inválido")

    @validator("cpf_cnpj", pre=True)
    def normalize_doc(cls, v):
        return ''.join([c for c in str(v) if c.isdigit()])
