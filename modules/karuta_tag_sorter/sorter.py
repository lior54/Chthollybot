import csv
import urllib.request


def sort_order(elem):
    return elem["series"], elem["character"], -int(elem["edition"]), -int(elem["quality"])

def karuta_sorter(link:str, exclude:list):
    data = urllib.request.urlopen(f"{link}")
    data = [l.decode("utf-8") for l in data.readlines()]
    cr = csv.DictReader(data)
    sort_card = {}
    tags = {}
    for row in cr:
        if row["tag"] in ["sort", ""]:
            if row["series"] not in sort_card:
                sort_card[row["series"]] = [row["code"]]
            else:
                sort_card[row["series"]].append(row["code"])
        elif not(row["tag"] in exclude or row["tag"] in tags):
            tags[row["series"]] = row["tag"]
                
    unknown = {}
    count = 0

    #sort dicts
    temp = list(tags.keys())
    temp.sort()
    tags = {i: tags[i] for i in temp}
    temp = list(sort_card.keys())
    temp.sort()
    sort_card = {i: sort_card[i] for i in temp}

    #making final list
    final = {}
    for series in sort_card:
        if series not in tags:
            unknown[series] = sort_card[series]
        elif tags[series] in final:
            final[tags[series]] += sort_card[series]
        else:
            final[tags[series]] = sort_card[series]

    #formatting output message
    send = ""
    for key in final:
        send += f'kt {key} {", ".join(final[key])}\n\n'
    send += "\n\nunknown cards to tag:\n"
    for key in unknown:
        send += f"{key}: {', '.join(unknown[key])}\n"
    return send

def karuta_duplicates(link:str):
    data = urllib.request.urlopen(f"{link}")
    data = [l.decode("utf-8") for l in data.readlines()]
    cr = csv.DictReader(data)
    