"""Demonstrate Basic List Syntax"""

# syntax is <list name>: list[<item type>]= list()

#Create a empty list
grocery_list: list[str]= list() #<-- constructor
grocery_list: list [str] = [] # <--literal
print ("Empty list: ")
print(grocery_list)

#Add to a list
grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")
print("After adding things")
print(grocery_list)

#Create list w Objects in it 
grocery_list2: list[str] = ["frosted flakes", "milk", "pizza"]
print("Already populated list: ")
print(grocery_list2)

grocery_list2.append("whipped cream")
print("Add another thing: ")
print(grocery_list2)

#Indexing 
print("Printing one item: ")
print(grocery_list[2])

#Modifying by Indexing 
x:str="cars"
x[2]="t"

grocery_list[0]= "cheerios"
print("Modifying: ")
print(grocery_list)


#length of grocery list
print("Length: ")
print(len(grocery_list))

#Removing a Item
grocery_list.pop(1)
print("Remove a item: ")
print (grocery_list)


def display (my_list:list[str])-> None:
    print(my_list)

x = display(["Anusha", "Jack", "Vrinda"])
print(x)

def create (word1: str, word2: str)-> list[str]:
    new_list: list[str] = [word1,word2]
    return new_list

x: list[str] = create("hello","world")
