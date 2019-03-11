from abc import ABC, abstractmethod
from typing import Union

import requests


class AbstractRequester(ABC):
    """Abstract class to extends to specific requests types."""

    def __init__(self, url: str):
        """Instances attributes for the abstract requesters."""
        self.url = url

    @abstractmethod
    def get_request(self) -> None:
        """Abstract method for a get request."""
        pass


class RequesterToSpaceX(AbstractRequester):
    """Extension from AbstractRequester, specially used to SpaceX API."""

    def get_request(self) -> Union[dict, list]:
        """Request to instance URL and return the content as a json."""
        request = requests.get(self.url)
        response = request.json()
        return response
