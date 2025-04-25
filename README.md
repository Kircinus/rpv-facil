# RPV Fácil

Sistema open source para automatizar o fluxo de gestão de RPVs nos municípios.

## Objetivo
Reduzir a burocracia e agilizar o atendimento de decisões judiciais de pequeno valor.

## Tecnologias
- OpenAI GPT para extração de dados
- Python, FastAPI
- OCR, PyMuPDF, pandas

## Como funciona
1. Recebe a intimação (PDF ou XML)
2. Extrai os dados essenciais
3. Gera relatório e integração com sistemas de pagamento

## Contribuições
Contribua com código, documentação ou ideias via Issues!

## Estrutura

``` bash
rpv-facil/
│
├── data/                    # Exemplos de intimações e pagamentos
├── src/
│   ├── extractor/           # Extratores de dados dos documentos
│   └── workflow/            # Lógica de fluxo automatizado
├── api/                     # Backend REST (planejado)
├── ui/                      # Interface web (se aplicável)
├── tests/
└── README.md
```
