# -*- coding: cp1252 -*-

"""
 2014 Biazus, Miller
 
 TREE IS A DICT: {A, [B, C]}
 WHERE:
     A IS THE NODE
     B IS NODE'S PARENT
     C IS NODE'S VALUE

 EACH NODE HAS A DEFAULT VALUE OF INFINITE (99999)
"""

INFINITE = 99999


# TREE ####

# initializing tree and root
def initTree(root):
    tree = {root: ["root", INFINITE]}
    print
    print "********** CREATING TREE..."
    return tree

# get the the parent of a given child
def getParent(child, tree):
    l = tree.get(child)
    print
    print ">>>>>>>>>> PARENT OF NODE " + str(child) + ": " +  str(l[0])
    return l[0]


# get all the children of a given parent
def getChildren(parent, tree):
    children_list = []
    for child_name, values in tree.iteritems():
        if values[0] == parent:
            children_list.append(child_name)
    print
    print ">>>>>>>>>> CHILDREN OF NODE " + str(parent) + ": " +  str(children_list)
    return children_list


# inserting node
def insertChild(child, parent, tree, value=INFINITE):
    if child in tree:
        pass
    else:
        tree[child] = [parent, value]
    print
    print "********** INSERTING " + str([child , parent, value])


# removing node and its children
def removeNode(node, tree):
    keys_to_delete = [k for k,v in tree.iteritems() if v[0]==node]
    for k in keys_to_delete:
        try:
            tree.pop(k, None)
            removeNode(k, tree)
        except KeyError:
            pass
    print
    print "********** REMOVING " + str(node)
    if node in tree:
        del tree[node]

# VALUES ####

def getValue(node, tree):
    l = tree.get(node)
    print
    print ">>>>>>>>>> VALUE OF NODE " + str(node) + ": " +  str(l[1])
    return l[1]

def setValue(node, tree, value):
    l = tree.get(node)
    l[1] = value
    print
    print ">>>>>>>>>> NEW VALUE OF NODE " + str(node) + ": " +  str(l[1])

# GENERAL ####

def printTree(tree):
    print
    print "-- TREE:"
    print tree
    print
