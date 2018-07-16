from Command import Command
from io import io

io = io()

def new_run(options, arg):
    """Adds a new issue with a priority level"""
    io.new(max(options), arg)

new = Command(name="new",aliases="mk,touch",options="12345",usage="[new/mk/touch -[priority] issue]", run=new_run)

def edit_run(options, arg):
    """Edit an issue"""
    #this one is a bit hacky since I only intended to allow a single argument
    args = arg.split(' ')
    priority = max(options) if len(options) != 0 else ""
    io.edit(args[0], priority, ' '.join(args[1:]))


edit = Command(name="edit",aliases="amend, change",options="12345",usage="[edit/amend/change] -[priority] [issue_id] [new description]", run=edit_run)

def show_run(options, arg):
    """Shows all issues, default all issues ordered ascending"""
    order = True
    status = None
    order = True if 'd' in options else False
    status = 'open' if 'o' in options else None
    status = 'closed' if 'c' in options else None
    if 'o' in options:
        status = "open"
    elif "c" in options:
        status = "closed"
    elif 'o' in options and "c" in options:
        status = None
    io.show_all(order, status)


show = Command(name="show",aliases="showall,ls,l,dir",options="ocad",usage="[show/showall/ls/l/dir] -[o]pen/[c]losed -[a]scending/[d]escending", run=show_run)

def add_run(options, arg):
    #also a bit hacky since I only intended to allow a single argument
    args = arg.split(' ')
    io.append(args[0], ' '.join(args[1:]))


add = Command(name="add",aliases="append",options="",usage="[add/append] [id] [description to add]", run=add_run)

def close_run(options, arg):
    io.close(arg)


close = Command(name="close",aliases="release,cl,rel",options="",usage="[release/cl/rel] [id]", run=close_run)
