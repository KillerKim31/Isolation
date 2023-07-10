init python:
    # Получить имя файла для предметов инвенторя
    def getFN(fn=""):
        return "inventory/" + fn + ".png"

    # Получить предмет из словаря объектов для инвенторя по его названию
    def getItem(itemName=""):
        return itemsData.get(itemName)

    # Добавить предмет в инвентарь.
    # Возвращает:
    #  1 - можно добавить
    # -1 - инвентарь полон
    #  0 - Попытка добавить предмет, который уже имеется в инвентаре
    def addItem(itemName):
        # Проверка на то, хватает ли места для добавления предмета в инвентарь
        if len(inventory) < limitInventory:
            if itemName not in inventory:
                inventory.append(itemName)
                return 1
            return 0
        return -1

    # Удалить предмет из инвентаря
    def removeItem(itemName=""):
        # Проверка наличия предмета в инвентаре
        if itemName in inventory:
            index = inventory.index(itemName)
            inventory.pop(index)

    def applyItem(itemName=""):
        if itemName in inventory:
            removeItem(itemName)
            lastItem = None
            renpy.hide_screen("inventory_screen")

    # Выбор или отмена выбора предмета из инвентаря для применения
    def selectItem(itemName=""):
        global lastItem
        # Проверка на наличие хотя бы 1 предмета в инвентаре
        if len(inventory) > 0:
            if (lastItem == None) or (lastItem != itemName):
                lastItem = itemName
            else:
                lastItem = None


init:
    # Флаг на то, открыт ли инвентарь
    $ openInventory = False
    # Размер инвенторя
    $ limitInventory = 7
    # Список для хранения названий предметов в инвенторе
    # $ inventory = ["cat_food", "key", "cable"]
    $ inventory = []
    # пустой последний нажатый предмет инвентаря
    $ lastItem = None
    
    # Словарь всех предметов, которые могут быть в инвентаре
    $ itemsData = {

        "cat_food": {
            "Name": "Кошачий корм",
            "Descript": "Консерва для кота. Пахнет приятно, но лучше не есть."
        },

        "key": {
            "Name": "Ключ от холодильника",
            "Descript": "Ключ, открывающий мир в блаженство вкусной еды."
        },

        "cable": {
            "Name": "Кабель питания",
            "Descript": "Шнур, по которому течёт живительный ток для устройств."
        },
    }

    # Анимация для отображения и скрытия панели инвентаря 
    transform show_hide_dissolve:
        # Блок для отображения панели
        on show:
            alpha .0
            yalign -.25
            parallel:
                linear .3 alpha 1.0
            parallel:
                linear .2 yalign .02
        # Блок для скрытия панели
        on hide:
            parallel:
                linear .2 yalign -.25
            parallel:
                linear .3 alpha .0


# Метка для помещения предмета в инвентарь
# Принимает в себя параметр newItem, являющийся строкой с названием предмета
label take_item(newItem):
    $ check = addItem(newItem)
    if check == 1:
        $ item = getItem(newItem)
        "Вы подобрали: [item[Name]]."
    elif check == -1:
        "Я не могу взять этот предмет, потому что мой инвентарь полон."
    else:
        "У меня такой предмет уже есть в инвентаре."
    return


label say_text(who=None, what=""):
    $ renpy.say(who, what)


#-------------Экраны для работы с инвентарём-------------#
#
#Экран с кнопкой для показа/сокрытия панели инвентаря
screen inventory_button:
    zorder 50
    imagebutton:
        xalign .97 yalign .02
        auto "inventory/bag_%s.png"
        if openInventory == False:
            action SetVariable("openInventory", True), Show("inventory_screen")
        else:
            action SetVariable("openInventory", False), SetVariable("lastItem", None), Hide("inventory_screen")

# Верхняя панель инвентаря
screen inventory_screen:
    frame at show_hide_dissolve:
        focus True
        background "inventory/panel.png"
        xsize 1500 ysize 200
        xalign .5
        padding(50, 35)
        # Элемент для отображения в виде списка
        viewport id "vp":
            xalign .5 yalign .5
            xsize 1300 ysize 120
            hbox:
                # Указание расстояния между объектами в горизонтальной области
                spacing 100
                for item in inventory:
                    imagebutton:
                        if item == lastItem:
                            idle Image(getFN(item + "_hover"))
                        else:
                            idle Image(getFN(item))
                        action Function(selectItem, item)