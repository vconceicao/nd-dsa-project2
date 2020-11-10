class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

class State():
    def __init__(self):
        self.visited_groups = {}
        
    def get_visited(self, group):
        return self.visited_groups.get(group.get_name)
    
    def set_visited(self,group):
        self.visited_groups[group.get_name] = group
        


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.index = 0

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index

    def increment_index(self):
        self.index+=1

    def is_groups_empty(self):
        return len(self.get_groups())==0

    def get_child(self):

        if len(self.groups) > self.index:
            return self.groups[self.index]


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user is None:
        print("The user can't be none")

    if group is None:
        print("The group can't be none")
        
    stack = Stack()
    state = State()
    stack.push(group)

    while group:
        if not state.get_visited(group):
            if user in group.get_users():
                return True
            state.set_visited(group)


        if not group.is_groups_empty() and group.get_child():
            group = group.get_child()
            stack.push(group)
        else:
            stack.pop()
            if not stack.is_empty():
                group = stack.top()
                group.increment_index()
            else:
                group = None
                
    return False


def test_find_subchild_user_in_subchild_group():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    result = is_user_in_group(sub_child_user, sub_child)
    print('test_find_subchild_user_subchild_group')
    print("The user {} is in {} : {}".format(sub_child_user, sub_child.get_name(),result))


def test_find_subchild_user_in_parent_group():
    parent = Group("parent")
    child = Group("child")
    child2 = Group("child2")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    child2.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    parent.add_group(child2)

    result = is_user_in_group(sub_child_user, parent)
    print('test_find_subchild_user_in_parent_group')
    print("The user {} is in {} : {}".format(sub_child_user, parent.get_name(),result))

def test_find_empty_user_in_parent_group():
    parent = Group("parent")
    child = Group("child")
    child2 = Group("child2")
    sub_child = Group("subchild")

    sub_child_user = ""
    child2.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    parent.add_group(child2)

    result = is_user_in_group(sub_child_user, parent)
    print('test_find_empty_user_in_parent_group')
    print("The user {} is in {} : {}".format(sub_child_user, parent.get_name(),result))

def test_find_user_in_none():
    print('test_find_user_in_none')

    sub_child_user = ""
    is_user_in_group(sub_child_user, None)



test_find_subchild_user_in_subchild_group()
#The user sub_child_user is in subchild : True
test_find_subchild_user_in_parent_group()
#The user sub_child_user is in parent : True
test_find_empty_user_in_parent_group()
#The user  is in parent : True
test_find_user_in_none()
#The group can't be none