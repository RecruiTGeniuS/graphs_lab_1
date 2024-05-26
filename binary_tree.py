# Файл с классом для представления бинарного дерева и фукнция для работы с этим деревом

# Подключение библиотек
import random
from collections import deque


# Класс узла
class Node:
    # Конструктор
    def __init__ (self, key):
        self.key = key
        self.left = None
        self.right = None

        # Координта по оси X и Y, требуются для отрисовки
        self.x = None
        self.y = None


# Класс бинарного дерева
class BinaryTree:
    # Конструктор
    def __init__ (self, root_node):
        self.root = root_node # Корень бинарного дерева

        # Массивы для хранения корней поддеревьев с максимальным/минимальным соотношением
        self.max_ratio_subtrees = [] 
        self.min_ratio_subtrees = []

    # Метод для поиска поддеревьев с максимальным/минимальным соотношениями (итерационный)
    def find_ratio_subtrees(self):
        if self.root is None:
            return 0
        
        # Вложенная функция, возвращающая высоту дерева/поддерева и кол-во его листьев
        def height_and_leaves(node):
            if node is None:
                return 0, 0
            
            stack = [(node, 1)]
            max_height = 0
            leaves = 0

            while stack:
                current, height = stack.pop()
                max_height = max(max_height, height)

                if current.left is None and current.right is None:
                    leaves += 1
                if current.right:
                    stack.append((current.right, height + 1))
                if current.left:
                    stack.append((current.left, height + 1))
            
            return max_height - 1, leaves
        
        # Вложенная функция, собирающая все поддереья в массив
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
        
        # Начальные условия для поиска соотношений
        subtrees = get_subtrees(self.root)
        max_ratio = float('-inf')
        min_ratio = float('inf')

        # Поиск максимальных/минимальных соотношений
        for subtree in subtrees:
            height, leaves = height_and_leaves(subtree)

            if leaves == 0:
                continue

            ratio = height / leaves

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


# Функция для поиска глубины дерева/поддерева (итерационная) нужна для отрисовки
def tree_depth(node):
    if node is None:
        return 0
    
    depth = 0
    queue = [(node, 1)]

    while queue:
        node, level = queue.pop()
        depth = max(depth, level)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return depth

# Функция для поиска ширины дерева/поддерева (итерационная) нужна для отрисовки
def tree_width(node):
    if node is None:
        return 0
    
    q = deque()
    q.append(node)
    width = 0

    while q:
        count = len(q)
        width = max(count, width)

        while (count != 0):
            count -= 1
            temp = q.popleft()
            if temp.left is not None:
                q.append(temp.left)
            
            if temp.right is not None:
                q.append(temp.right)

    return width

# Функция для поиска кол-ва детей у дерева/поддерева (итерационная) нужна для отрисовки
def count_nodes(node):
    if node is None:
        return 0

    node_count = 0
    queue = [node]

    while queue:
        node = queue.pop(0)
        node_count += 1  
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return node_count

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

    return node_dict[nodes[0]] # Возвращает корень дерева


# Две функции для создания случайного дерева с соблюдением примерного баланса
# Функия для случайной вставки
def insert_random(root, key):
    if root is None:
        return Node(key)
    
    elif random.random() < 0.5:  # Вероятность вставки в левое поддерево
        root.left = insert_random(root.left, key)

    else:  # Вероятность вставки в правое поддерево
        root.right = insert_random(root.right, key)

    return root

# Функция для создания случайного дерева с соблюдением примерного баланса
def random_build_tree(size):
    root = None

    for i in range(1, size + 1):
        root = insert_random(root, i)

    return root


# Функция для создания дерева на основе данных, введённых с клавиатуры
def input_build_tree():
    nodes = list(map(int, input("Введите узлы дерева через пробел:     ").strip().split()))
    left_children = list(map(int, input("Введите левых потомков через пробел:  ").strip().split()))
    right_children = list(map(int, input("Введите правых потомков через пробел: ").strip().split()))

    if not nodes:
        return None

    node_dict = {key: Node(key) for key in nodes}

    for i, key in enumerate(nodes):
        if left_children[i] != 0:
            node_dict[key].left = node_dict.get(left_children[i], None)
        if right_children[i] != 0:
            node_dict[key].right = node_dict.get(right_children[i], None)

    return node_dict[nodes[0]] # Возвращает корень дерева
