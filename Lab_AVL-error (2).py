import sys 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 


def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 
        
        updateHeight(node)
        
        balance = getBalance(node)

        if balance > 1 and getBalance(node.left) >= 0:
            return rotate_right(node) 
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node)
        elif balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node) 
        
        return node
    def getMinValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def delete(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            temp = self.getMinValueNode(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)
            updateHeight(node)
            balance = getBalance(node)
            if balance > 1 and getBalance(node.left) >= 0:
                return rotate_right(node)
            if balance > 1 and getBalance(node.left) < 0:
                node.left = rotate_left(node.left)
                return rotate_right(node)
            if balance < -1 and getBalance(node.right) <= 0:
                return rotate_left(node)
            if balance < -1 and getBalance(node.right) > 0:
                node.right = rotate_right(node.right)
                return rotate_left(node)
            return node
    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)

    
        
avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50,25,64, 70, 80, 90]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")

print(avl.inorder(avl.root))
print(getBalance(avl.root))

while True:
    
    print("Opciones")
    print("1. agregar nodo")
    print("2. eliminar nodo")
    print("3. ver balance")
    print("4. ver altura")
    print("5. salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        valor = int(input("Ingrese el valor a agregar: "))
        avl.insert(valor)
        print("Árbol después de la inserción:", avl.inorder(avl.root))
    elif opcion == "2":
        valor = int(input("Ingrese el valor a eliminar: "))
        avl.delete(avl.root, valor)
        print("Árbol después de la eliminación:", avl.inorder(avl.root))
    elif opcion == "3":
        print("Balance del árbol:", getBalance(avl.root))
    elif opcion == "4":
        print("Altura del árbol:", getHeight(avl.root))
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
