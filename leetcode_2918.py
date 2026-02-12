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
            # Format: "(2011-2019)" or "(2011- )"
            runtime = runtime.strip("()")
            parts = runtime.split("-")

            show_start = int(parts[0].strip())

            end_part = parts[1].strip()
            if end_part == "" or end_part == " ":
                show_end = float("inf")
            else:
                show_end = int(end_part)

            # Overlap: show was in production during [startYear, endYear]
            if show_start <= endYear and show_end >= startYear:
                result.append(show["name"])

        page += 1

    return result
