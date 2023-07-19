from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        id="8",
        product_name="Aspirin",
        company_name="Galena Biopharma",
        manufacturing_date="2021-02-22",
        expiration_date="2024-03-14",
        serial_number="KZ63 800H NM4B ZOWB YYUI",
        storage_instructions="instrucao 8",
    )

    assert str(product) == (
        f"The product {product.id} - {product.product_name} "
        f"with serial number {product.serial_number} "
        f"manufactured on {product.manufacturing_date} "
        f"by the company {product.company_name} "
        f"valid until {product.expiration_date} "
        "must be stored according to the following instructions: "
        f"{product.storage_instructions}."
    )
