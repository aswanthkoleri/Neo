def Todo(action,todolist,message="",removeItemNo=-1):
    if action=="add":
        # first count the no items in list increment it and add the new no to the list
        # itemNo=len(item)
        todolist.append((message,0))
    if action=="done":
        # find the item with that item 
        itemNo=removeItemNo-1
        todolist.pop(itemNo)
    
    
