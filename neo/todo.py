def Todo(action,todolist,message="",removeItemNo=-1):
    if action=="add":
        # first count the no items in list increment it and add the new no to the list
        # itemNo=len(item)
        todolist.append((message,0))
    if action=="done":
        # find the item with that item 
        itemNo=removeItemNo-1
        # print("Done",itemNo)
        # print(todolist)
        item=todolist[itemNo]
        todolist.pop(itemNo)
        todolist.append((item[0],1))
    if action=="remove":
        itemNo=removeItemNo-1
        # item=todolist[itemNo]
        todolist.pop(itemNo)
    if action=="remove_all":
        todolist=[]
    if action=="undone":
        itemNo=removeItemNo-1
        item=todolist[itemNo]
        todolist.pop(itemNo)
        todolist.insert(0,(item[0],0))
    return
    
def displayTodo(message,todolist):
    for i,content in enumerate(todolist):
        if content[1]==0:
            message+=str(i+1)+". :cross_mark: "+content[0]+"\n\n\n"
        elif content[1]==1:
            message+=str(i+1)+". :check_mark: ~~"+content[0]+"~~\n\n\n"
    return message
        
