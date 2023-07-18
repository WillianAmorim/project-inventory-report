from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        id="8",
        product_name="Aspirin",
        company_name="Galena Biopharma",
        manufacturing_date="2021-02-22",
        expiration_date="2024-03-14",
        serial_number="KZ63 800H NM4B ZOWB YYUI",
        storage_instructions="instrucao 8",
    )
    assert product.id == "8"
    assert product.product_name == "Aspirin"
    assert product.company_name == "Galena Biopharma"
    assert product.manufacturing_date == "2021-02-22"
    assert product.expiration_date == "2024-03-14"
    assert product.serial_number == "KZ63 800H NM4B ZOWB YYUI"
    assert product.storage_instructions == "instrucao 8"
