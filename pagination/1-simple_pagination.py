#!/usr/bin/env python3
"""This module provides a helper function for pagination calculations."""

import csv
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
        Get page

        Args:
            page (int): page number
            page_size (int): number of items per page
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
