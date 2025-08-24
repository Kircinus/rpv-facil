from src.rpv_facil.extractor.xml_extractor import parse_xml

def test_parse_xml():
    data = parse_xml("data/samples/sample_rpv.xml")
    assert data["processo"].startswith("0800")
    assert "R$" in data["valor"]
