import os
import pytest
import crud

@pytest.fixture(autouse=True)
def reset_products_file():
    """Reset products.json before each test"""
    crud._save_data([])
    yield
    # Cleanup after test
    if os.path.exists(crud.FILE_PATH):
        os.remove(crud.FILE_PATH)