import time
import random

# Класс узла
class Node:
    # Конструктор
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

        self.correlation = None # Соотношение высота/листья

        # Координаты по оси X и Y, требуются для отрисовки
        self.x = None
        self.y = None


# Класс Бинарного дерева
class BinaryTree:
    # Конструктор
    def __init__(self, root_node):
        self.root = root_node  # Корень бинарного дерева
        self.max_ratio_subtrees = []  # Поддеревья с максимальным соотношением
        self.min_ratio_subtrees = []  # Поддеревья с минимальным соотношением

    def find_subtrees_with_extreme_ratios(self):
        if self.root is None:
            return 0

        def height_and_leaves(node):
            if not node:
                return 0, 0
            stack = [(node, 1)]
            max_height = 0
            leaf_count = 0
            while stack:
                current, height = stack.pop()
                max_height = max(max_height, height)
                if not current.left and not current.right:
                    leaf_count += 1
                if current.right:
                    stack.append((current.right, height + 1))
                if current.left:
                    stack.append((current.left, height + 1))
            return max_height - 1, leaf_count

        def get_subtrees(node):
            queue = [node]
            subtrees = []
            while queue:
                current = queue.pop(0)
                if current.left or current.right:
                    subtrees.append(current)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            return subtrees

        subtrees = get_subtrees(self.root)
        max_ratio = float('-inf')
        min_ratio = float('inf')

        for subtree in subtrees:
            height, leaves = height_and_leaves(subtree)
            if leaves == 0:
                continue
            ratio = height / leaves
            #print(root.key, ':', ratio) # tut
            if ratio > max_ratio:
                max_ratio = ratio
                self.max_ratio_subtrees = [subtree]
            elif ratio == max_ratio:
                self.max_ratio_subtrees.append(subtree)
            
            if ratio < min_ratio:
                min_ratio = ratio
                self.min_ratio_subtrees = [subtree]
            elif ratio == min_ratio:
                self.min_ratio_subtrees.append(subtree)


# Функция для создания дерева на основе данных из файла
def file_build_tree(file):
    with open(file, 'r') as tree_file:
        nodes = list(map(int, tree_file.readline().split()))
        left_children = list(map(int, tree_file.readline().split()))
        right_children = list(map(int, tree_file.readline().split()))

    if not nodes:
        return None

    node_dict = {key: Node(key) for key in nodes}

    for i, key in enumerate(nodes):
        if left_children[i] != 0:
            node_dict[key].left = node_dict[left_children[i]]
        if right_children[i] != 0:
            node_dict[key].right = node_dict[right_children[i]]

    return node_dict[nodes[0]]

def insert_random(root, key):
    if root is None:
        return Node(key)
    elif random.random() < 0.5:  # Вероятность вставки в левое поддерево
        root.left = insert_random(root.left, key)
    else:  # Вероятность вставки в правое поддерево
        root.right = insert_random(root.right, key)
    return root

def create_random_tree(size):
    root = None
    for _ in range(size):
          # Здесь 100 - максимальное значение ключа
        root = insert_random(root, _)
    return root

def depth(node):
    if node is None:
        return 0
     
    left_depth = depth(node.left)
    right_depth = depth(node.right)
    
    return max(left_depth, right_depth) + 1


def max_depth(root):
    if root is None:
        return 0

    depth = 0
    queue = [(root, 1)]  # Очередь для обхода в ширину, включая уровень каждого узла

    while queue:
        node, level = queue.pop(0)
        depth = max(depth, level)  # Обновляем глубину на каждом уровне

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return depth
# Пример использования:
#random_tree = create_random_tree(500000)  # Создание случайного дерева с 10 узлами


root = Node(1)
root.left = Node(2)
root.left.left = Node(6)
root.right = Node(3)
root.right.right = Node(4)
root.right.left = Node(5)

# root = file_build_tree('trees.txt')
# print(1)

tree = BinaryTree(root)

st = time.time()
g = max_depth(root)
en = time.time()

t = en - st
print(g)

print("Поддеревья с максимальным соотношением (высота/листья):")
for subtree in tree.max_ratio_subtrees:
    print(subtree.key)

print("Поддеревья с минимальным соотношением (высота/листья):")
for subtree in tree.min_ratio_subtrees:
    print(subtree.key)

print("Время работы алгоритма:", t)