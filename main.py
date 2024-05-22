# main файл

# Иморт других файлов проекта
import binary_tree as bt
import drawing as dr
import file_generate as fg

# Создание дерева
# root = bt.Node(1)
# root.left = bt.Node(2)
# root.left.left = bt.Node(9)
# root.right = bt.Node(3)
# root.right.left = bt.Node(4)
# root.right.right = bt.Node(5)
# root.right.left.left = bt.Node(6)
# root.right.left.right = bt.Node(7)


# Дерево 2
# root = bt.Node(1)
# root.left = bt.Node(2)
# root.right = bt.Node(3)
# root.right.right = bt.Node(4)
# root.right.right.right = bt.Node(5)
# root.right.right.right = bt.Node(6)
# root.right.right.left = bt.Node(7)
# root.right.right.left.left = bt.Node(8)
# root.right.right.left.left.left = bt.Node(9)


# Дерево 3
root = bt.Node(1)
root.left = bt.Node(2)
root.right = bt.Node(3)
root.left.left = bt.Node(4)
root.left.right = bt.Node(5)
root.left.right.left = bt.Node(8)
root.left.left.left = bt.Node(6)
root.left.left.left.left = bt.Node(7)

root.right.left = bt.Node(7)
root.right.right = bt.Node(8)
root.right.right.left = bt.Node(10)
root.right.right.left.left = bt.Node(11)
root.right.right.left.right = bt.Node(12)
root.right.right.left.left.left = bt.Node(13)
root.right.right.left.left.right = bt.Node(14)
root.right.right.right = bt.Node(9)
root.right.right.right.right = bt.Node(16)



tree = bt.BinaryTree(root)
tree.find_correlation(root)
print(tree.max_correlation)
#print(bt.count_nodes(root.right) - 1)
print(bt.getMaxWidth(root))

dr.draw_tree(root)
