import re
from concurrent.futures import ThreadPoolExecutor
import requests

BASE_URL = "https://jsonmock.hackerrank.com/api/tvseries?page="
YEAR_RE = re.compile(r'\((\d{4})(\s*-\s*(\d{4})?)?\s*\)')


def _fetch(page):
    return requests.get(f"{BASE_URL}{page}").json()


def showsInProduction(startYear, endYear):
    first = _fetch(1)
    total_pages = first["total_pages"]

    with ThreadPoolExecutor(max_workers=total_pages) as pool:
        pages = [first] + list(pool.map(_fetch, range(2, total_pages + 1)))

    result = []
    for data in pages:
        for show in data["data"]:
            match = YEAR_RE.search(show["runtime_of_series"])
            if not match:
                continue

            show_start = int(match.group(1))
            if show_start < startYear:
                continue

            if match.group(2) is None:
                show_end = show_start
            elif match.group(3) is None:
                show_end = None
            else:
                show_end = int(match.group(3))

            if endYear == -1:
                if show_end is None:
                    result.append(show["name"])
            else:
                if show_end is not None and show_end <= endYear:
                    result.append(show["name"])

    result.sort()
    return result
