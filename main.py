# main файл

# Подключение библиотек
import time

# Иморт других файлов проекта
import binary_tree as bt
import drawing as dr
import file_generate as fg


fg.generate_tree_file(100)

root = bt.file_build_tree('trees.txt') 

#print(bt.tree_width(root))
root = bt.random_build_tree(30)
#root = bt.input_build_tree()
tree = bt.BinaryTree(root)


start_time = time.time()
tree.find_ratio_subtrees()
end_time = time.time()
elapsed_time = end_time - start_time


print(elapsed_time)

dr.draw_tree(root)
for node in tree.max_ratio_subtrees:
    dr.draw_tree(node)


for node in tree.min_ratio_subtrees:
    dr.draw_tree(node)
