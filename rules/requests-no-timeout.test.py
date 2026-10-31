import requests


def bad():
    # ruleid: requests-no-timeout
    requests.get("http://example.test")
    # ruleid: requests-no-timeout
    requests.post("http://example.test", json={"a": 1})


def ok():
    # ok: requests-no-timeout
    requests.get("http://example.test", timeout=5)
    # ok: requests-no-timeout
    requests.post("http://example.test", json={"a": 1}, timeout=(3, 10))
