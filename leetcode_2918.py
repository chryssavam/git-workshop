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

            # Remove (I) or (II) prefix if present
            runtime = re.sub(r'\(I{1,2}\)\s*', '', runtime).strip()

            # Strip outer parentheses
            runtime = runtime.strip('()')

            if '-' in runtime:
                parts = runtime.split('-')
                show_start = int(parts[0].strip())
                end_part = parts[1].strip()
                if end_part == '':
                    # Still in production, e.g. "(2020-)"
                    show_end = None
                else:
                    show_end = int(end_part)
            else:
                # Single year, e.g. "(2020)"
                show_start = int(runtime.strip())
                show_end = show_start

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
