from typing import Dict


class HttpRequest:
    def __init__(self, header: Dict = None, body: Dict = None, params: Dict = None):
        self.header = header
        self.body = body
        self.params = params
