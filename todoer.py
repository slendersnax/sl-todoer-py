from slender_todo import Slender_Todo
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    main_group = parser.add_mutually_exclusive_group()

    main_group.add_argument("-l", "--list",
                        choices=["all", "not-done", "done"],
                        metavar="STATUS",
                        help="show the current list - you must use one of the keywords to specify which items you want to see")

    main_group.add_argument("-n", "--new", nargs="*",
                        metavar="ITEM",
                        help="insert a new item into the list - use \"\" to make sure that it's stored exactly like you want it to be, or don't use them because it works like that too")

    main_group.add_argument("-dn", "--done", nargs="*",
                        metavar="IDs",
                        help="mark the items with the IDs given (separated by space) as 'done'")

    main_group.add_argument("-del", "--delete", nargs="*",
                        metavar="IDs",
                        help="deletes the items with the IDs given (separated by space)")

    main_group.add_argument("-delmul", "--delete-multiple",
                        choices=["all", "not-done", "done"],
                        metavar="STATUS",
                        help="deletes all items with the specified status (all is a status, yes)")

    main_group.add_argument("-v", "--version",
                        action="store_true")

    return parser

def main():
    todo_handler = Slender_Todo()

    parser = get_arguments()
    args = parser.parse_args()

    if args.version:
        todo_handler.print_version()
    elif args.list:
        todo_handler.select_all(args.list)
    elif args.new:
        todo_handler.add(args.new)
    elif args.done:
        todo_handler.make_done(args.done)
    elif args.delete:
        todo_handler.delete(args.delete)
    elif args.delete_multiple:
        todo_handler.delete_multi(args.delete_multiple)

if __name__ == "__main__":
    main()
