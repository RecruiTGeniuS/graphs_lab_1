import pygame as pg
import binary_tree as bt

# Функция по отрисовки круга (рабочая, но радиус не трогать)
def draw_node_circle(surface, ex_color, in_color, x, y, radius, text, text_color):
    # Чтобы текст помещался в кружок
    if radius > 10:
        text_size = len(str(text))

        pg.draw.circle(surface, ex_color, (x, y), radius, 0)
        pg.draw.circle(surface, in_color, (x, y), radius - 1, 0)
        format_text = pg.font.Font(pg.font.match_font('verdana'), radius - 5 - text_size)
        in_text = format_text.render(str(text), 1, text_color)
        text_rect = in_text.get_rect(center=(x, y))
        surface.blit(in_text, text_rect)



# Функция отрисовки дерева с узла 
def draw_tree(node_root):
    if node_root.key > 1000:
        return 0
    
    nodes = bt.count_nodes(node_root)
    tree_width = bt.tree_width(node_root)
    tree_depth = bt.tree_depth(node_root)

    pg.init()

    # Параметры основного экрана
    WIDTH = 900
    HEIGHT = 900

    # Параметры виртуальной поверхности
    
    if nodes / tree_width > 5:
        VWIDHT = WIDTH + 5000 * tree_width # В теории можно брать по параметрам того какая у дерева ширина
    elif nodes / tree_width > 200:
        VWIDHT = WIDTH + 5000 * tree_width
    else:
        VWIDHT = WIDTH + 500 * tree_width

    VHEIGHT = HEIGHT + 50 * tree_depth # Ну а тут какая высота

    # Шаг для изменения длин/наклона веток
    X_STEP = 20
    Y_STEP = 15

    # Начальные координаты корня дерева
    node_root.x = VWIDHT / 2
    node_root.y = 100



    # Основной экран
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE | pg.DOUBLEBUF | pg.HWSURFACE, pg.NOFRAME)
    pg.display.set_caption('Binary Tree')
    # ------------------------------------


    # Виртуальная поверхность на экране
    virtual_surface = pg.Surface((VWIDHT, VHEIGHT))
    virtual_surface.fill('white')

    # Копия поверхности для трансформации
    virtual_surface_transform = virtual_surface

    # Взятие экземляра класса Rect для того чтобы перемещать/масштабировать поверхность
    virtual_surface_rect = virtual_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 + (HEIGHT - 400)))

    # Идентификатор взятия пользователем виртуальной поверхности
    virtual_surface_grab = False

    # Отрисовка кружков и линий на виртуальной поверхности
    # pg.draw.circle(virtual_surface, 'black', (500, 500), 10, 0)
    # pg.draw.line(virtual_surface, 'black', (500, 500), (570, 570), 2)
    # pg.draw.circle(virtual_surface, 'black', (570, 570), 10, 0)

    def traversal_draw(node):
        if node is None:
            return 0
        
        
        node_childrens = bt.count_nodes(node) - 1
        x_offset = X_STEP * node_childrens / 1.1 + X_STEP
        y_offset = Y_STEP + (Y_STEP * 2) + (Y_STEP * (node_childrens / nodes))

        if node.left != None and node.right != None:
            pg.draw.line(virtual_surface, 'black', (node.x, node.y), (node.x - x_offset, node.y + y_offset))
            pg.draw.line(virtual_surface, 'black', (node.x, node.y), (node.x + x_offset, node.y + y_offset))
            draw_node_circle(virtual_surface, 'black', 'white', node.x, node.y, 20, node.key, 'black')
            node.left.x = node.x - x_offset
            node.left.y = node.y + y_offset
            node.right.x = node.x + x_offset
            node.right.y = node.y + y_offset
        if node.left != None and node.right == None:
            pg.draw.line(virtual_surface, 'black', (node.x, node.y), (node.x - x_offset, node.y + y_offset))
            draw_node_circle(virtual_surface, 'black', 'white', node.x, node.y, 20, node.key, 'black')
            node.left.x = node.x - x_offset
            node.left.y = node.y + y_offset
        if node.left == None and node.right != None:
            pg.draw.line(virtual_surface, 'black', (node.x, node.y), (node.x + x_offset, node.y + y_offset))
            draw_node_circle(virtual_surface, 'black', 'white', node.x, node.y, 20, node.key, 'black')
            node.right.x = node.x + x_offset
            node.right.y = node.y + y_offset
        if node.left == None and node.right == None:
            draw_node_circle(virtual_surface, 'black', 'white', node.x, node.y, 20, node.key, 'black')

        
        traversal_draw(node.left)
        traversal_draw(node.right)
        
        
    traversal_draw(node_root)

    # -------------------------------------


    # Отрисовка рамки для виртуальной поверхности
    pg.draw.line(virtual_surface, 'black', (0,0), (0, VHEIGHT-2), 2)
    pg.draw.line(virtual_surface, 'black', (0, VHEIGHT-2), (VWIDHT, VHEIGHT-2), 2)
    pg.draw.line(virtual_surface, 'black', (VWIDHT-2, VHEIGHT-2), (VWIDHT-2, 0), 2)
    pg.draw.line(virtual_surface, 'black', (VWIDHT, 0), (0, 0), 2)
    # -------------------------------------



    # Цикл работы программы
    running = True
    while running:

        # Обработка событий
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if virtual_surface_rect.collidepoint(event.pos):
                        virtual_surface_grab = True

                if event.button == 4 or event.button == 5:
                    zoom = 1.11 if event.button == 4 else 0.9
                    mx, my = event.pos
                    left = mx + (virtual_surface_rect.left - mx) * zoom
                    if left > -5500: # кажется можно брать по тому что прибавляешь +- heigh (около того)
                        right = mx + (virtual_surface_rect.right - mx) * zoom
                        top = my + (virtual_surface_rect.top - my) * zoom
                        bottom = my + (virtual_surface_rect.bottom - my) * zoom
                        virtual_surface_rect = pg.Rect(left, top, right-left, bottom-top)
                        virtual_surface_transform = pg.transform.smoothscale(virtual_surface, virtual_surface_rect.size)
                        print(left, right, top, bottom)
                    

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    virtual_surface_grab = False

            if event.type == pg.MOUSEMOTION:
                if virtual_surface_grab == True:
                    virtual_surface_rect.move_ip(event.rel)


            if event.type == pg.QUIT:
                running = False


        # Обновление и отрисовка
        screen.fill('white')
        screen.blit(virtual_surface_transform, virtual_surface_rect)
        # ----------------------------------


        pg.display.flip()
        

    pg.quit()