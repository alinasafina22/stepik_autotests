import pytest
from product_page import add_to_card
from product_page import final_check


def test_guest_can_add_product_to_basket():
    add_to_card()
    assert final_check() == True

