import os, json, tempfile
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from typing import List, Optional
from src.rpv_facil.workflow.pipeline import ingest_file, make_report
from src.rpv_facil.integration.payments import to_bank_payload

app = FastAPI(title="RPV Fácil", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename) as tmp:
        tmp.write(await file.read())
        tmp.flush()
        data, status = ingest_file(tmp.name)
    return JSONResponse({"status": status, "data": data})

class ReportRequest(BaseModel):
    items: List[dict]
    format: Optional[str] = "csv"

@app.post("/report")
async def report(req: ReportRequest):
    out = make_report(req.items, req.format or "csv")
    return FileResponse(out, filename=os.path.basename(out))

@app.post("/payments/payload")
async def payments_payload(req: ReportRequest):
    return JSONResponse(to_bank_payload(req.items))

@app.post("/workflow/ingest")
async def workflow_ingest(path: str = Form(...)):
    data, status = ingest_file(path)
    return JSONResponse({"status": status, "data": data})
