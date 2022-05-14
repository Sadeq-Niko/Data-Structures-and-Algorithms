
class node:#کلاس معرفی گره
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None
        self.height=0


class avl_tree:#درخت avl
    def __init__(self):
        self.root=None

    #صرفا جهت نمایش
    def __repr__(self):
        if self.root == None: return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = ' ' * int((2 ** (cur_height - 1)))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.value != None:
                    buf = ' ' * int((5 - len(str(n.value))) / 2)
                    cur_row += '%s%s%s' % (buf, str(n.value), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left_child != None:
                    next_nodes.append(n.left_child)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right_child != None:
                    next_nodes.append(n.right_child)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content


    def insert(self,value):#برای دادن ورودی به درخت
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,current_node):
        if value<current_node.value:
            if current_node.left_child==None:
                current_node.left_child=node(value)
                current_node.left_child.parent=current_node
                self._inspect_insertion(current_node.left_child)
            else:
                self._insert(value,current_node.left_child)
        elif value>current_node.value:
            if current_node.right_child==None:
                current_node.right_child=node(value)
                current_node.right_child.parent=current_node
                self._inspect_insertion(current_node.right_child)
            else:
                self._insert(value,current_node.right_child)
        else:
            print("this value already exist!")


    def delete_value(self,value):
        return self.delete_node(self.find(value))

    def delete_node(self,node):


        def min_node(n):#پیدا کردن کوچکترین نود سمت چپ یک عنصر
            current=n
            while current.left_child!=None:
                current=current.left_child
            return current


        def num_children(n):#پیدا کردن تعداد فرزندان یک نود
            num_children=0
            if n.left_child!=None:
                num_children+=1
            if n.right_child!=None:
                num_children+=1
            return num_children


        node_parent= node.parent
        node_children=num_children(node)
        #چندین حالت وجود دارد که سناریوی هر کدام متفاوت است
        if node_children==0:
            if node_parent.left_child==node:
                node_parent.left_child=None
            else:
                node_parent.right_child=None

        if node_children == 1:
            if node.left_child!=None:
                child=node.left_child
            else:
                child=node.right_child
            if node_parent.left_child==node:
                node_parent.left_child=child
            else:
                node_parent.right_child=child
            child.parent=node_parent

        if node_children==2:
            successor=min_node(node.right_child)
            node.value=node.right_child.value
            self.delete_node(successor)


            return


        if node_parent!=None:
            node_parent.height=1+max(self.get_height(node_parent.left_child),self.get_height(node_parent.right_child))#چرا 1+مکس
            self._inspect_deletion(node_parent)

    #در اینجا متد های سه روش مختلف نمایش دادن پیاده سازی شده اند
    def print_tree_postorder(self):
        if self.root!=None:
            self._print_tree_postorder(self.root)


    def _print_tree_postorder(self,current_node):
        if current_node!=None:
            self._print_tree_postorder(current_node.left_child)
            self._print_tree_postorder(current_node.right_child)
            #print(str(current_node.value))
            print ('%s'%(str(current_node.value)))

    def print_tree_preorder(self):
        if self.root != None:
            self._print_tree_preorder(self.root)

    def _print_tree_preorder(self, current_node):
        if current_node != None:
            #print(str(current_node.value))
            print ('%s'%(str(current_node.value)))
            self._print_tree_preorder(current_node.left_child)
            self._print_tree_preorder(current_node.right_child)

    #روش پیمایش inorder روش بیس و پایه ی این پروژه هست
    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,current_node):
        if current_node!=None:
            self._print_tree(current_node.left_child)
            #print(str(current_node.value))
            print ('%s, h=%d'%(str(current_node.value),current_node.height))
            self._print_tree(current_node.right_child)

    #پیدا کردن ارتفاع به صورت بازگشتی
    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0


    def _height(self,current_node,current_height):
        if current_node==None:
            return current_height
        left_height=self._height(current_node.left_child,current_height+1)
        right_height=self._height(current_node.right_child,current_height+1)
        return max(left_height,right_height)


    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,current_node):
        if value==current_node.value:
            return True
        elif value<current_node.value and current_node.left_child!=None:
            return self._search(value,current_node.left_child)
        elif value>current_node.value and current_node.right_child!=None:
           return self._search(value,current_node.right_child)
        else:
            return False


    def find(self,value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left_child != None:
            return self._find(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._find(value, current_node.right_child)
        #else:
         #   return None




    #avl _ functions
    #این متد اینسرشن را برای درخت avl مناسب میکند و کمک میکند تا بعد از هر ورودی درخت چک شود و در صورت نیاز تغییر اعمال شود
    def _inspect_insertion(self,current_node,path=[]):
        if current_node.parent==None:return
        path=[current_node]+path

        left_height=self.get_height(current_node.parent.left_child)
        right_height=self.get_height(current_node.parent.right_child)

        if abs(left_height-right_height)>1:
            path=[current_node.parent]+path
            self._rebalance_node(path[0],path[1],path[2])
            return


        new_height=1+current_node.height
        if new_height>current_node.parent.height:
            current_node.parent.height=new_height

        self._inspect_insertion(current_node.parent,path)

    #مانند متد بالا به حذف عناصر کمک میکند
    def _inspect_deletion(self,current_node):
        if current_node==None:return

        left_height = self.get_height(current_node.left_child)
        right_height = self.get_height(current_node.right_child)

        if abs(left_height-right_height)>1:
            y=self.taller_child(current_node)
            x=self.taller_child(y)
            self._rebalance_node(current_node,y,x)

        self._inspect_deletion(current_node.parent)

    #برای بالانس کردن دوباره استفاده میشود و از متد های چرخش استفاده میکند
    def _rebalance_node(self,z,y,x):
        if y==z.left_child and x==y.left_child:
            self._right_rotate(z)
        elif y==z.left_child and x==y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y==z.right_child and x==y.right_child:
            self._left_rotate(z)
        elif y==z.right_child and x==y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception("z,y,x node not recognized!")


    def _right_rotate(self,z):
        sub_root=z.parent
        y=z.left_child
        x=y.right_child
        y.right_child=z
        z.parent=y
        z.left_child=x
        if x!=None:
            x.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        z.height=+max(self.get_height(z.left_child),self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),self.get_height(y.right_child))


    def _left_rotate(self,z):
        sub_root=z.parent
        y=z.right_child
        x=y.left_child
        y.left_child=z
        z.parent=y
        z.right_child=x
        if x!=None:
            x.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        z.height = +max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))


    def get_height(self,current_node):
        if current_node==None:return 0
        return current_node.height

    #برگرداندن بلندرین فرزند
    def taller_child(self,current_node):
        left=self.get_height(current_node.left_child)
        right=self.get_height(current_node.right_child)
        return current_node.left_child if left>=right else current_node.right_child


#def fill_tree(tree,num_elems=100,max_int=1000):
 #   from random import randint
  #  for _ in range(num_elems):
   #     current_elem=randint(0,max_int)
    #    tree.insert(current_elem)
    #return tree


tree=avl_tree()
#tree.root=node(1)
#tree.root.left_child=node(2)
#tree.root.right_child=node(3)
#tree.root.left_child.left_child=node(4)
#tree.root.left_child.right_child=node(5)

#tree.insert(10)
#tree.insert(5)
#tree.insert(7)
#tree.insert(12)
#tree.insert(3)
#tree.insert(2)
#tree.insert(1)
#tree.insert(11)

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)


print(tree)
print("inorder")
tree.print_tree()
print("preorder")
tree.print_tree_preorder()
print("postorder")
tree.print_tree_postorder()
#tree.print_inorder(tree.root)
#print("tree height:"+str(tree.height()))
#for i in range(10):
   # print("inserting %d"%i)
  #  tree.insert(i)
 #   print(tree)
#for i in range(10):
  #  print("deleting %d"%i)
 #   tree.delete_value(i)
 #   print(tree)
print(tree.search(4))
tree.delete_value(3)
print(tree)