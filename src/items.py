from item import Item


items = [
    Item("lighter",
         "A mechanical device for lighting a cigarette, cigar, or pipe.", 0),
]


def getitemsbyids(ids):
    return [items[id] for id in ids]
