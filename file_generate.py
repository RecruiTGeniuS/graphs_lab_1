import random


# Количество узлов для деревьев:
num_nodes_1 = 10
num_nodes_2 = 100
num_nodes_3 = 500
num_nodes_4 = 1000
num_nodes_5 = 5000
num_nodes_6 = 10000
num_nodes_7 = 50000
num_nodes_8 = 100000
num_nodes_9 = 500000
num_nodes_10 = 1000000



# Функция, генерирующая случайно дерево дерево
def generateTree(num_nodes):

    if num_nodes > 2:
        
        nodes = []  # Массив узлов
        left = []   # Массив левых потомков
        right = []  # Массив правых потомков

        сurrent_child = 0 # Переменная, определяющая потомков для узлов


        # Добавление элементов в массив узлов
        for i in range(num_nodes):
            nodes.append(i + 1)
        
        # Первая случайная генерация потомков - для корня 
        rand_num = random.randint(0, 1) 

        # Если на место выпал 0
        if rand_num == 0:
            left.append(0)
            right.append(2)
            сurrent_child = 3

        # Если на место выпало число
        else:
            left.append(2)
            rand_num = random.randint(0, 1)

            if rand_num == 0:
                right.append(0)
                сurrent_child = 3
                
            else:
                right.append(3)
                сurrent_child = 4


        # Вторая случайная генерация - для первого уровня дерева
        rand_num = random.randint(0, 1)

        # Если на место выпал 0
        if rand_num == 0:

            if сurrent_child == 3:
                left.append(0)
                right.append(сurrent_child)

            else:
                left.append(0)
                right.append(random.randrange(0, 5, 4))
                
        # Если на место выпало число        
        else:
            left.append(сurrent_child)

            if сurrent_child == 3:
                right.append(random.randrange(0, 5, 4))

            else:
                right.append(random.randrange(0, 6, 5))
                
            
                
        # Обновление переменной для определения потомков 
        сurrent_child = max(max(left), max(right)) + 1
        

        # Третья случайная генерация - для оставшихся узлов
        for i in range(2, num_nodes):
            
            if сurrent_child <= num_nodes:
                rand_num = random.randint(0,1)

                if rand_num == 0:

                    if max(max(left), max(right)) - nodes[i] > 0:
                        left.append(0)
                        rand_num = random.randrange(0, сurrent_child + 1, сurrent_child)
                        right.append(rand_num)

                        if rand_num != 0:
                            сurrent_child += 1

                        else:
                            continue
                        
                    else:
                        left.append(0)
                        right.append(сurrent_child)
                        сurrent_child += 1

                else:
                    left.append(сurrent_child)
                    сurrent_child += 1

                    if сurrent_child <= 7:
                        rand_num = random.randrange(0, сurrent_child + 1, сurrent_child)
                        right.append(rand_num)

                        if rand_num != 0:
                            сurrent_child += 1

                        else:
                            continue
                    else:
                        right.append(0)             

            else:
                left.append(0)
                right.append(0)

        return nodes, left, right
    
    else:
        print("Ошибка! Нужно задать больше чем 2 узла")



# Генерация дерева
tree_list = generateTree(10)


# Запись в файл
with open('trees.txt', 'w') as trees_file:

    for i in range(3):
        for j in range(10):
            trees_file.write(str(tree_list[i][j]))
            trees_file.write(' ')
        trees_file.write('\n')


