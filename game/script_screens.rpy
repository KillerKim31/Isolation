# Спальня
screen bedroom():
    sensitive not (renpy.get_screen("say") or renpy.get_screen("choice"))    # Отключение чувствительности экрана при активном экране диалога или выбора
    # imagemap - карта изображений, которая позволяет на одном изображении создать прямоугольные области,
    # по которым можно наводиться и кликать с дальнейшим выполнением действий (action)
    imagemap:
        # Параметр auto позволяет автоматически определить 3 изображения:
            # ground - основное изображение, которое выводится всегда
            # idle - изображение, которое выводится для определённых прямоугольных областей
            # hover - изображение при наведении курсора на область
        # %s - это модификатор, который позволяет python понять, что за место него нужно поставить строковое значение
        auto "images/bg/bedroom_%s.png"
        
        # Экш SensitiveIf позволяет проверить условие и включить чувствительность к наведению и клику,
        # удобен для отображения области изображения при определённых условиях
        # Экшн Call позволяет перейти к указанной метке с передачей ей параметра объекта на экране, который был кликнут
        # Команда mouse позволяет поменять курсор мышки на значение, определённое в словаре config.mouse из файла init
        hotspot(1085, 320, 90, 100) action SensitiveIf(not drinkWater), Call("bedroom_label", "pills") mouse "put" # Стакан и таблетки
        hotspot(775, 845, 235, 225) action SensitiveIf(drinkWater), Show("coridor", dissolve), Hide("bedroom") mouse "put" # Стрелка назад
        hotspot(275, 285, 790, 460) action Call("bedroom_label", "sofa") mouse "put" # Диван
        hotspot(600, 10, 240, 285) action Call("bedroom_label", "poster") mouse "put" # Плакат
        hotspot(180, 760, 310, 245) action Call("bedroom_label", "sticks") mouse "put" # Костёр из палок
        hotspot(1180, 665, 620, 400) action Call("bedroom_label", "clother") mouse "put" # Куча одежды
        hotspot(1350, 145, 245, 270) action Call("bedroom_label", "computer") mouse "put" # Монитор


# Коридор
screen coridor:
    sensitive not (renpy.get_screen("say") or renpy.get_screen("choice"))    # Отключение чувствительности экрана при активном экране диалога или выбора
    imagemap:
        auto "images/bg/coridor_%s.png"
        
        hotspot(770, 155, 395, 410) action Call("coridor_label", "exit") mouse "put" # Металлическая дверь
        hotspot(380, 205, 145, 480) action Show("bedroom", dissolve), Hide(renpy.current_screen().name) mouse "put" # Дверь в спальню
        hotspot(1420, 225, 140, 490) action Show("cookingroom", dissolve), Hide(renpy.current_screen().name) mouse "put" # Дверь на кухню
        hotspot(1665, 360, 195, 695) action Show("guestroom", dissolve), Hide(renpy.current_screen().name) mouse "put" # Дверь в гостинную


# Кухня
screen cookingroom:
    sensitive not (renpy.get_screen("say") or renpy.get_screen("choice"))    # Отключение чувствительности экрана при активном экране диалога или выбора
    imagemap:
        auto "images/bg/cookingroom_%s.png"
        
        hotspot(690, 465, 90, 80) action SensitiveIf(not takeCatFood), Call("kitchen_label", "catFood") mouse "put" # Консерва с кормом
        hotspot(1190, 320, 330, 220) action SensitiveIf(not openFridge), Call("kitchen_label", "fridge") mouse "put" # Цепь на холодильнике
        hotspot(130, 940, 130, 90) action SensitiveIf(not putCatFood), Call("kitchen_label", "cat dish") mouse "put" # Миска для кота
        hotspot(550, 210, 220, 160) action Call("kitchen_label", "picture") mouse "put" # Картина
        hotspot(80, 160, 250, 435) action Call("kitchen_label", "poster") mouse "put" # Плакат

        hotspot(840, 815, 240, 250) action Show("coridor", dissolve), Hide(renpy.current_screen().name) mouse "put" # Стрелка назад

    if putCatFood:
        imagebutton:
            idle "images/bg/cat_eat.png"
            focus_mask True
            action Call("kitchen_label", "cat dish") mouse "put"


# Гостинная
screen guestroom:
    sensitive not (renpy.get_screen("say") or renpy.get_screen("choice"))    # Отключение чувствительности экрана при активном экране диалога или выбора
    imagemap:
        auto "images/bg/guestroom_%s.png"

        hotspot(1725, 740, 90, 70):
            if not putKey:
                # Экшн If позволяет сделать разветвление действий для кнопки при определённом условии
                # Если выполняется несколько действий в одной ветке, то необходимо обрамлять их квадратными скобками []
                action If(not putCatFood,
                    [ SetVariable("seeCat", True), Call("guest_label", "key") ],
                    [ SetVariable("putKey", True), Call("guest_label", "key") ]
                )
                mouse "put" # Ключ
        hotspot(745, 115, 160, 295) action Call("guest_label", "clock") mouse "put" # Часы
        hotspot(345, 560, 255, 135) action Call("guest_label", "music player") mouse "put" # Музыкальный проигрыватель
        hotspot(1030, 245, 365, 365) action Call("guest_label", "server") mouse "put" # Сервер
        hotspot(1625, 250, 250, 280) action Call("guest_label", "picture") mouse "put" # Картина

        hotspot(685, 805, 255, 260) action Show("coridor", dissolve), Hide(renpy.current_screen().name) mouse "put" # Стрелка назад
    
    if not putCatFood:
        imagebutton:
            focus_mask True
            idle "cat"
            hover "cat_light"
            action SetVariable("seeCat", True), Call("guest_label", "key") mouse "put"


# Экран с запиской
screen show_leter(name):
    modal True
    imagebutton:
        idle "images/letters/" + name + ".png"
        action Return(True), Hide(renpy.current_screen().name, dissolve)
