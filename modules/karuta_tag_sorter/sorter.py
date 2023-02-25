import csv
import urllib.request

def sort_order(elem):
    return elem[4], elem[3], -int(elem[2]), -int(elem[5])

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
    data = [i.split('","') for i in data]
    data[1:] = sorted(data[1:], key=sort_order)
    data = ['","'.join(i) for i in data]
    cr = csv.DictReader(data)
    cards = {}
    for row in cr:
        if row["character"] + ", " + row["series"] not in cards:
            cards[row["character"] + ", " + row["series"]] = {"1":0, "2":0, "3":0, "4":0, "5":0}
        cards[row["character"] + ", " + row["series"]][row["edition"]] += 1
    
    send = ""
    for char in cards:
        to_write = []
        for edition in cards[char]:
            if cards[char][edition] > 1:
                to_write.append(edition)
        if len(to_write) > 0:
            send = send + char + ": Ed"
            for edition in to_write:
                send = send + f" {edition}({cards[char][edition]}),"
            send = send[:-1] + "\n"
    print(send)
    return send