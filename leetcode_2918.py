import re
import requests


def showsInProduction(startYear, endYear):
    result = []
    page = 1
    total_pages = 1

    while page <= total_pages:
        resp = requests.get(
            f"https://jsonmock.hackerrank.com/api/tvseries?page={page}"
        )
        data = resp.json()
        total_pages = data["total_pages"]

        for show in data["data"]:
            runtime = show["runtime_of_series"]

            # Search for the year pattern directly, skipping any (I)/(II) prefix
            # Matches: (2020-2021), (2020-), (2020)
            match = re.search(r'\((\d{4})(\s*-\s*(\d{4})?)?\s*\)', runtime)
            if not match:
                continue

            show_start = int(match.group(1))

            if match.group(2) is None:
                # Single year format: (2020)
                show_end = show_start
            elif match.group(3) is None:
                # Still in production: (2020-)
                show_end = None
            else:
                # Range: (2020-2021)
                show_end = int(match.group(3))

            # Filter: started in startYear or later
            if show_start < startYear:
                continue

            if endYear == -1:
                # Only want shows still in production
                if show_end is None:
                    result.append(show["name"])
            else:
                # Must have ended and ended in endYear or earlier
                if show_end is not None and show_end <= endYear:
                    result.append(show["name"])

        page += 1

    result.sort()
    return result
