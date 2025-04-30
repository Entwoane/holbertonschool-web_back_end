#!/usr/bin/env python3
"""This module provides a helper function for pagination calculations."""

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end index for pagination.
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.
    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
                        and end index (exclusive) for the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: A list of data items for the requested page.
        """
        assert (
            isinstance(page, int)
            and page > 0
            and isinstance(page_size, int)
            and page_size > 0
        )
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end] if start < len(data) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns pagination information and data for a given page.

        Args:
        page (int): The current page number (default is 1).
        page_size (int): The number of items per page (default is 10).

        Returns:
        dict: A dictionary containing the page size, current page, data,
            next page number, previous page number, and total number of pages.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
