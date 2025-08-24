from src.rpv_facil.workflow.pipeline import ingest_file

def test_ingest_xml():
    data, status = ingest_file("data/samples/sample_rpv.xml")
    assert status == "ok"
    assert data["processo"]
    assert float(data["valor"]) > 0
