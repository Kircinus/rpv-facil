import json
import typer
from .workflow.pipeline import ingest_file, make_report

app = typer.Typer(add_completion=False)

@app.command()
def extract(path: str):
    data, status = ingest_file(path)
    typer.echo(json.dumps({"status": status, "data": data}, ensure_ascii=False, indent=2))

@app.command()
def report(input: str, fmt: str = "csv"):
    items = json.loads(open(input, "r", encoding="utf-8").read())
    out = make_report(items, fmt)
    typer.echo(out)

if __name__ == "__main__":
    app()
