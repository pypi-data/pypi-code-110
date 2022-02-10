#!/usr/bin/python

version = '0.1.0'
def json_search(json_data, key: str):
    path = []
    if isinstance(json_data, dict):
        for k in json_data.keys():
            if k == key:
                path.append([k])
            child = json_data[k]
            if key not in str(child):
                continue
            for subpath in json_search(child, key):
                path.append([k] + subpath)

    if isinstance(json_data, list):
        for i, child in enumerate(json_data):
            if key not in str(child):
                continue
            for subpath in json_search(child, key):
                path.append([i] + subpath)


    return path

if __name__ == '__main__':
    import json
    from argparse import ArgumentParser

    parser = ArgumentParser(usage='usage: json_search [-h] (-f FILE | -s STR) -k KEY')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', help='json file', type=str)
    group.add_argument('-s', '--str', help='json string', type=str)
    parser.add_argument('-k', '--key', help='the key to search', type=str, required=True)

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            data = json.load(f)
    elif args.str:
        data = json.loads(args.str)

    for ret in json_search(data, args.key):
        print(ret)