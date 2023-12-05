#!/usr/bin/python3

""" Module 7-add_item.py """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
        main - Entry Point function
    """
    args = list()
    idx = 1
    path = "add_item.json"

    try:
        args = load_from_json_file(path)
    except:
        pass

    while idx < len(sys.argv):
        args.append(sys.argv[idx])
        idx += 1

    with open(path, 'a', encoding="utf-8") as f:
        save_to_json_file(args, path)

if __name__ == '__main__':
    main()
