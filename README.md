# sl-todoer-py
A simple todo app in Python based on the Simple CRUD checkpoint found here: https://roadmap.sh/full-stack

### usage
`python todoer.py -COMMAND ARGS`

where the possible commands are

`-h, --help` to print all the commands and their usage

`-v, --version` to show the current version

`-l, --list STATUS` to print the current items that have a status of...STATUS (possible values are `all, not-done, done`). I really didn't have a better idea for the variable name, I know 'all' isn't a status

`-n, --new ITEM` to add a new item

`-dn, --done IDs` to mark one or multiple items as 'done' based on their IDs

`-del, --delete IDs` to delete one or multiple items based on their IDs

`-delmul, --delete-multiple STATUS` to delete multiple items using the same STATUS keywords from the `list` command

### notes

I think that I cheated a bit by using the built-in `sqlite3` module, and I plan on making an alternative that doesn't use it in the future.
