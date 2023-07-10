
init python:
    # Класс инвентарь
    class Inventory:
        # Конструктор класса
        def __init__(self, items, limit, lastItem):
            self.items = items
            self.limit = limit
            self.lastItem = lastItem
        
        # Добавить предмет в инвентарь.
        # Возвращает:
        #  1 - можно добавить
        # -1 - инвентарь полон
        #  0 - Попытка добавить предмет, который уже имеется в инвентаре
        def addItem(itemName):
            # Проверка на то, хватает ли места для добавления предмета в инвентарь
            if len(self.items) < limit:
                if itemName not in self.items:
                    self.items.append(itemName)
                    return 1
                return 0
            return -1

        # Удалить предмет из инвентаря
        def removeItem(itemName=""):
            # Проверка наличия предмета в инвентаре
            if itemName in self.items:
                index = self.items.index(itemName)
                self.items.pop(index)

        def applyItem(itemName=""):
            if self.lastItem in self.items:
                removeItem(itemName)
                self.lastItem = None
                renpy.hide_screen("inventory_screen")

        # Выбор или отмена выбора предмета из инвентаря для применения
        def selectItem(itemName=""):
            # Проверка на наличие хотя бы 1 предмета в инвентаре
            if len(self.items) > 0:
                if (self.lastItem == None) or (self.lastItem != itemName):
                    self.lastItem = itemName
                else:
                    self.lastItem = None

    # Словарь всех предметов, которые могут быть в инвентаре
    itemsData = {
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

    # Создание экземпляра класса Inventory, являющийся инвентарём игрока
    inventory = Inventory(["cat_food", "key", "cable"], 7, None)
            

init python:
    # Получить имя файла для предметов инвенторя
    def getFN(fn=""):
        return "inventory/" + fn + ".png"

    # Получить предмет из словаря объектов для инвенторя по его названию
    def getItem(itemName=""):
        return itemsData.get(itemName)

    
init:
    # Флаг на то, открыт ли инвентарь
    $ openInventory = False

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
    $ check = inventory.addItem(newItem)
    if check == 1:
        # Создание локальной переменной метки take_item
        $ item = getItem(newItem)
        "Вы подобрали: [item[Name]]."
    elif check == -1:
        "Я не могу взять этот предмет, потому что мой инвентарь полон."
    else:
        "У меня такой предмет уже есть в инвентаре."
    return


#-------------Экраны для работы с инвентарём-------------#
#
#Экран с кнопкой для показа/сокрытия панели инвентаря
screen inventory_button:
    zorder 50       # Задание уровня отображения экрана
    imagebutton:
        xalign .97 yalign .02
        auto "inventory/bag_%s.png"     # Автоматическая инициализация 3-х изображений с подстановкой через %s
        if openInventory == False:
            action SetVariable("openInventory", True), Show("inventory_screen")
        else:
            action SetVariable("openInventory", False), SetVariable("inventory.lastItem", None), Hide("inventory_screen")

# Верхняя панель инвентаря
screen inventory_screen:
    frame at show_hide_dissolve:
        background "inventory/panel.png"        # Замена стандартной картинки frame на другую
        xsize 1500 ysize 200
        xalign .5
        padding(50, 35)         # Задание внутренних отступов панели frame
        # Элемент для формирования объектов в виде списка
        viewport id "vp":
            xalign .5 yalign .5
            xsize 1300 ysize 120
            hbox:
                spacing 100     # Указание расстояния между объектами в горизонтальной области
                for item in inventory.items:
                    imagebutton:
                        if item == inventory.lastItem:
                            idle Image(getFN(item + "_hover"))
                        else:
                            idle Image(getFN(item))
                        action Function(inventory.selectItem)