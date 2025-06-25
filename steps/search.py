from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pages import Pages


def search_stream(pages: Pages, value: str):
    # Click in the search icon
    pages.twich_home_page.browse_tab.wait().click()

    # Input StarCraft II
    pages.browse_page.search_input.wait().input(value)

    if not pages.browse_page.search_category_result(value).wait(no_exception=True).is_visible:
        pages.browse_page.search_result(value).wait(timeout=10).click()
    else:
        pages.browse_page.search_category_result(value).wait(no_exception=True).click()
