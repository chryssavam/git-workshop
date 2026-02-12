import re
import requests

YEAR_RE = re.compile(r'\((\d{4})(\s*-\s*(\d{4})?)?\s*\)')


def showsInProduction(startYear, endYear):
    session = requests.Session()
    result = []
    page = 1
    total_pages = 1

    while page <= total_pages:
        data = session.get(
            f"https://jsonmock.hackerrank.com/api/tvseries?page={page}"
        ).json()
        total_pages = data["total_pages"]

        for show in data["data"]:
            runtime = show.get("runtime_of_series")
            if not runtime:
                continue
            match = YEAR_RE.search(runtime)
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

        page += 1

    result.sort()
    return result
