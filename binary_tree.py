


# # Класс узла
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#         self.correlation = None


#     # Глубина

#     # Ширина

#     # Алгоритм

#     # Добавление узла

# # Семантически - кайф, фактически - а зачем? Не создаст ли больше проблем?
# class BinaryTree(object):
#     def __init__(self, root):
#         self.root = Node(root)


# # Обход в глубину
# def pre_order(node):
#     if node is None:
#         return 0
    
#     print(node.key)
#     pre_order(node.left)
#     pre_order(node.right)
    

# # Украденная функия поиска глубины (рабочая, может понадобиться для отрисовки) для задания фигачь тут отсюда -1, чтобы типа высота по вершинам
# def maxDepth(node):
#     if node is None:
#         return 0
 
#     else:
 
#         # Compute the depth of each subtree
#         lDepth = maxDepth(node.left)
#         rDepth = maxDepth(node.right)
 
#         # Use the larger one
#         if (lDepth > rDepth):
#             return lDepth+1
#         else:
#             return rDepth+1

# # Украденная функция поиска кол-ва листьев 
# def num_leaves(root):
#     count = 0
#     if root.left is None and root.right is None:
#         count += 1
#     if root.left:
#         count += num_leaves(root.left)
#     if root.right:
#         count += num_leaves(root.right)

#     return count




  


# # Типа алгоритм, связанный с заданием
# def min_max_subtrees(root):


#     # По идее, если эту функцию делат как метод класса BinaryTree то эти значения могут пойти как его атрибуты
#     min_correlation = (maxDepth(root) - 1) / num_leaves(root)
#     max_correlation = (maxDepth(root) - 1) / num_leaves(root)
#     min_trees_keys = []
#     max_trees_keys = []

#     def alg(node):
#         nonlocal min_correlation, max_correlation 
#         print(max_correlation)
#         if node is None:
#             return 0
        
#         node.correlation = (maxDepth(node) - 1) / num_leaves(node)
#         print(node.key, ': ', node.correlation)

#         if node.correlation == 0:
#             pass
#         elif node.correlation < min_correlation:
#             min_correlation = node.correlation
#             min_trees_keys.clear()
#             min_trees_keys.append(node)
#         elif node.correlation == min_correlation:
#             min_trees_keys.append(node)
        

#         if node.correlation > max_correlation:
#             max_correlation = node.correlation
#             max_trees_keys.clear()
#             max_trees_keys.append(node)
#         elif node.correlation == max_correlation:
#             max_trees_keys.append(node)
#         alg(node.left)
#         alg(node.right)
#         return min_correlation, max_correlation

#     alg(root)

#     return min_correlation, max_correlation, max_trees_keys, min_trees_keys
# # arr_nodes = []
# # for i in range(1, 5):
# #     arr_nodes.append(Node(i))

# # l = [0, 3, 0, 0]
# # r = [2, 4, 0, 0]

# # for i in range(4):
# #     if l[i] != 0:
# #         arr_nodes[i].left = Node(l[i])

# #     if r[i] != 0:
# #         arr_nodes[i].right = Node(r[i])




# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# n2 = root.right.left = Node(4)
# root.right.right = Node(5)
# root.right.left.left = Node(6)
# root.right.left.right = Node(7)
# root.right.left.right.left = Node(8)
# root.right.left.right.right = Node(9)
# root.right.right.right = Node(10)
# root.right.right.right.right = Node(11)
# root.right.right.right.right.right = Node(12)
# root.right.right.right.right.right.left = Node(13)
# root.right.right.right.right.right.right = Node(14)
# root.right.right.right.right.right.right.left = Node(15)
# root.right.right.right.right.right.right.right = Node(16)


# print('-----------')
# print(maxDepth(n2) - 1)
# print(num_leaves(n2))

# print(min_max_subtrees(root)[0])





# def min_max_subtrees(root):
#     min_ratio = float('inf')
#     max_ratio = float('-inf')
#     min_trees = []
#     max_trees = []

#     def helper(node):
#         nonlocal min_ratio, max_ratio
#         if node is None:
#             return (float('inf'), float('-inf'))
#         left_height = height(node.left)
#         right_height = height(node.right)
#         left_leaves = count_leaves(node.left)
#         right_leaves = count_leaves(node.right)
#         if left_leaves == 0 or right_leaves == 0:
#             return (float('inf'), float('-inf'))
#         ratio = max(left_height / left_leaves, right_height / right_leaves)
#         if ratio < min_ratio:
#             min_ratio = ratio
#             min_trees.clear()
#             min_trees.append(node)
#         elif ratio == min_ratio:
#             min_trees.append(node)
#         if ratio > max_ratio:
#             max_ratio = ratio
#             max_trees.clear()
#             max_trees.append(node)
#         elif ratio == max_ratio:
#             max_trees.append(node)
#         min_left, max_left = helper(node.left)
#         min_right, max_right = helper(node.right)
#         return (min(min_left, min_right, ratio), max(max_left, max_right, ratio))

#     helper(root)
#     return min_ratio, max_ratio, min_trees, max_trees











# РАБОЧИЙ КОД
from collections import deque



class Node:
    # Конструктор
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.correlation = None # Соотношение высота/листья
        self.x = None # Координата узла по оси Х. Требуется для отрисовки
        self.y = None # Координата узла по оси Y

class BinaryTree:
    # Конструктор
    def __init__ (self, root_node):
        self.root = root_node # Корень бинарного дерева
        
        # Минимальное и максимальное соотношения высота/листья
        self.min_correlation = correlation(root_node)
        self.max_correlation = correlation(root_node)
        
        # Массивы узлов, соотношения которых соответсвуют минимальному и максимальному
        self.min_corr_nodes = []
        self.max_corr_nodes = []
        
    # Метод ищущий минимальное и максимальное соотношения в дереве, а также сответствующие им узлы
    def find_correlation(self, node):
        if node is None:
            return 0
        
        node.correlation = correlation(node)
        
        if node.correlation == 0:
            pass
        else:
            if node.correlation < self.min_correlation:
                self.min_correlation = node.correlation
                self.min_corr_nodes.clear()
                self.min_corr_nodes.append(node)
            elif node.correlation == self.min_correlation:
                self.min_corr_nodes.append(node)
            
                
            if node.correlation > self.max_correlation:
                self.max_correlation = node.correlation
                self.max_corr_nodes.clear()
                self.max_corr_nodes.append(node)
            elif node.correlation == self.max_correlation:
                self.max_corr_nodes.append(node)
        
        self.find_correlation(node.left)
        self.find_correlation(node.right)
        
        
    
# Функция для поиска глубины дерева/поддерева
def depth(node):
    if node is None:
        return 0
     
    left_depth = depth(node.left)
    right_depth = depth(node.right)
    
    return max(left_depth, right_depth) + 1

# Функция для поиска ширины дерева/поддерева Украдена(https://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/)
def getMaxWidth(root):
    if root is None:
        return 0
    q = deque()
    maxWidth = 0
 
    q.append(root)
 
    while q:
        count = len(q)
 
        maxWidth = max(count, maxWidth)
 
        while (count is not 0):
            count = count-1
            temp = q.popleft()
            if temp.left is not None:
                q.append(temp.left)
 
            if temp.right is not None:
                q.append(temp.right)
 
    return maxWidth
        
# Функция для поиска кол-ва листьев у дерева/поддерева
def count_leaves(node):
    count = 0
    if node.left is None and node.right is None:
        count += 1
    if node.left:
        count += count_leaves(node.left)
    if node.right:
        count += count_leaves(node.right)
    
    return count

# Функия, считающая колиство узлов в дереве/поддереве
def count_nodes(node):
    if not node:
        return 0
    
    return 1 + count_nodes(node.left) + count_nodes(node.right)
    
# Функция, вычисляющая отношение высота/листья
def correlation(node):
    return ((depth(node) - 1) / count_leaves(node))
    


# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(9)
# root.right = Node(3)
# root.right.left = Node(4)
# root.right.right = Node(5)
# root.right.left.left = Node(6)
# root.right.left.right = Node(7)

# tree = BinaryTree(root)
# tree.find_correlation(root)
# print(tree.max_correlation)
# print(count_nodes(root.right) - 1, 'Листья')
# print(getMaxWidth(root))


# to-do:
# * Ввод с клавиатуры
# * Ввод с файла
# * Связь с выводом
# * Подсчёт времени работы алгоритма и вывод его
    

