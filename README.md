# RPV Fácil

Sistema **open source** para automatizar o fluxo de gestão de **Requisições de Pequeno Valor (RPVs)** em municípios.

## Objetivo
Reduzir a burocracia e agilizar o atendimento de decisões judiciais de pequeno valor — do recebimento à liquidação — com **rastreamento, validação e relatórios**.

## Tecnologias
- **Python 3.11+**
- **FastAPI** (API REST)
- **PyMuPDF** (extração de texto de PDF) + **OCR opcional** (pytesseract/pdf2image)
- **pandas** para relatórios (CSV/Excel)
- **Pydantic** (modelos e validação)

## Como funciona
1. Recebe a intimação (PDF/XML) via upload na API ou pasta `data/in/`.
2. Extrai dados essenciais (nº processo, exequente, CPF/CNPJ, valor, vara, data, ente, conta).
3. Valida e normaliza (máscaras, datas, moedas).
4. Gera relatório (CSV/Excel) e registra o **workflow** (status, logs e justificativas).
5. Integra com sistema de pagamentos (webhook/arquivo) — **plug-in de integração**.

## Execução rápida
```bash
uv venv && source .venv/bin/activate   # ou python -m venv .venv
uv pip install -e .[api,ocr]           # ou pip install -e .[api,ocr]
uvicorn api.main:app --reload
# abrir: http://localhost:8000/docs
```

## Estrutura
```
rpv-facil/
├─ data/
│  ├─ in/                  # uploads / arquivos de exemplo
│  ├─ out/                 # relatórios
│  └─ samples/             # fixtures para testes
├─ src/
│  ├─ extractor/           # extratores PDF/XML e normalização
│  ├─ workflow/            # orquestração e estados
│  └─ integration/         # conectores de pagamento (mock/real)
├─ api/                    # FastAPI (endpoints)
├─ ui/                     # UI simples (Streamlit) opcional
├─ tests/                  # pytest
├─ pyproject.toml
├─ .env.example
├─ Dockerfile
└─ README.md
```

## Endpoints (principais)
- `POST /extract` — Upload de PDF/XML, retorna JSON normalizado.
- `POST /report` — Gera CSV/Excel a partir de uma lista de RPVs.
- `POST /workflow/ingest` — Inicia workflow de um arquivo já no `data/in`.
- `GET /health` — Saúde da aplicação.

## Avisos
- Este repositório **não é consultoria jurídica**. Confirme com a legislação e normativos locais.
- Dados de exemplo são fictícios.
