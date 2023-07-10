# Игра начинается здесь:
label start:
    scene start_image with fade
    player """
    Ааа, жутко болит голова!
    
    Что за ужас вчера произошёл?
    """

    menu:
        "Полежать ещё чуток.":
            player "Вздремну ещё часик, может поможет."
            pause 1.0

            "Прошёл час."

            player "Ааа, нифига не помогло, стало вроде ещё хуже!"
            menu:
                "Может ещё полежать?":
                    player """
                    Ну может организму нужно больше времени для восстановления?
                    
                    Посплю ещё.
                    """
                    pause 1.0

                    "Вы продолжаете лежать, и через какое-то время снова просыпааетесь."

                    player """
                    Аааааааа, да нифига не легчает!
                    
                    Что же за напасть такая?
                    """
                    menu:
                        "Лежать до последнего, пока не станет лучше!!!":
                            player "Если мне что и поможет, так это отдых."
                            pause 1.0
                            scene sleeping with fade

                            """
                            Вы лежите так долго, что голова перестаёт вас беспокоить.
                            
                            Вы просто умерли.
                            
                            Конец!
                            """

                            scene black with fade
                            return
                        "Встать с дивана.":
                            jump start.look_up
                "Встать с дивана.":
                    jump start.look_up
        "Встать с дивана.":
            jump start.look_up

    # Локальная метка, вложенная в глобальную метку start
    label .look_up:
        player "А, чёрт подери, надо хотя бы пойти попить."

    show screen inventory_button with dissolve
    show screen bedroom with dissolve

    hide start_image with dissolve
    window hide
    $ renpy.pause(hard=True)
    return


label bedroom_label(obj=""):
    # Отображение панели диалога в автоматическом режиме
    # Если поставить в значение show, то панель будет на долю секунды
    # промелькивать, когда было передано obj = ""
    window auto
    if obj == "":
        pass
    elif obj == "pills":
        player """
        Ой как голова раскалывается. Хорошо что, кто-то оставил здесь воду и аспирин.
        
        Ох, полегчало.

        А что за бумажка здесь лежит?
        """

        # Сокрытие панели диалога, чтобы её не было видно, когда никто ничего не говорит
        window hide
        # Вызов экрана для отображения записки
        # После закрытия экрана будет возвращено значение
        $ value = renpy.call_screen("show_leter", "page1")

        if value:
            player """
            Вот чёрт.
                
            Есть сразу захотелось! Надо найти кухню.
            """
        $ drinkWater = True

    # Ветки слов ГГ при описании кликабельных объектов без дальнейшей логики
    elif obj == "sofa":
        player "Жёсткий диван, от которого у меня всё болит."
        $ hide_all_screens()
    elif obj == "poster":
        player "Забавный плакат. Какие крутые банки у девушки!"
    elif obj == "computer":
        if inventory.lastItem == "cable":
            player "Вот тебе кабель, дружочек-компьюторочек."
            $ computerCable = True
            $ inventory.applyItem(inventory.lastItem)
        else:
            player "О, какой крутой компьютер! Вот только у него нет питания."
    elif obj == "clother":
        player "Ужас какой бардак тут!"
    elif obj == "sticks":
        player """
        Имитированный костёр из светящихся палок.
        
        Достаточно оригинально и не вредит экологии.
        """

    window hide
    # Жесткая пауза, которая не позволяет пользователю кликом мышки перейти дальше по коду.
    # Здесь жёсткая пауза не даёт закончиться текущей метке
    $ renpy.pause(hard=True)
    return


label coridor_label(obj=""):
    window auto
    if obj == "":
        pass
    elif obj == "exit":
        player "Нифиговая такая дверина! Даже из пушки не сломать её."

    window hide
    $ renpy.pause(hard=True)
    return


label kitchen_label(obj=""):
    window auto
    if obj == "":
        pass

    elif obj == "catFood":
        if not seeCat:
            player """
            Кошачий корм?

            Нет уж, это я точно есть не буду!
            """
        else:
            player "Тот зверь может тоже хочет есть, ведь никого здесь больше нет. Возьму-ка я для него баночку."
            $ takeCatFood = True
            call take_item("cat_food")

    elif obj == "cat dish":
        if inventory.lastItem == "cat_food":
            player "Вот тебе котяра хавчик - ешь."
            $ putCatFood = True
            $ inventory.applyItem(inventory.lastItem)
        elif putCatFood:
            player "Кушай кушай и меня не трогай."
        else:
            player "Судя по миске, здесь где-то бродит кот."

    elif obj == "fridge":
        if inventory.lastItem == "key":
            player "Да будут открыты врата холодной еды."
            $ openFridge = True
            $ inventory.applyItem(inventory.lastItem)

            scene finaly_end with dissolve
            hide screen cookingroom with dissolve
            hide screen inventory_button with dissolve
            hide screen inventory_screen with dissolve

            $ renpy.notify("Вы достигли конца прототипа игры.")
            
            "Поздарвляем, вы прошли прототип игры до правильного конца."

            "На этом всё, спасибо, что играли с нами."

            scene black with fade
            return
        else:
            player "Вот же чёрт! Кто запирает холодильник на замок?"


    elif obj == "poster":
        player '"Все мухи бляхи" - а кто такие мухи?'

    elif obj == "picture":
        player "Забавная картина. Выглядит, как моя школа, из которой я выпускался."

    window hide
    $ renpy.pause(hard=True)
    return


label guest_label(obj=""):
    window auto
    if obj == "":
        pass
    elif obj == "key":
        if putCatFood:
            player "Как говорится, пост держи, а обед по расписанию."
            $ hasKeyFridge = True
            $ inventory.addItem("key")
        else:
            player """
            Ах! Этот кот строго охраняет этот ключ.
            
            Мне его не достать просто так.
            """

    elif obj == "clock":
        player """
        ГОСПАДИ!
        
        Часы встали.
        """
    elif obj == "picture":
        player """
        В этой картине забавно то, что кажется, будто это окно.

        Тогда я должен быть на очень высоком этаже.
        """
    elif obj == "music player":
        # Разделение набора действий при флаге playerOn
        # Прописывать оператор if в блоке menu  для самих вариантов выбора невозможно - вылазит ошибка
        # Однако использовать ветвление внутри варианта можно
        if playerHasCabel:
            if playerOn:
                menu:
                    "Выключить музло.":
                        stop music fadeout .5
                        $ playerOn = False
                    "Забрать шнур.":
                        $ playerHasCabel = False
                        $ playerOn = False
                        stop music fadeout .5
                        call take_item("cable")
                    "Уйти.":
                        pass
            else:
                menu:
                    "Включить музло.":
                        play music "sounds/megavegan.mp3" fadein .1 loop
                        $ playerOn = True
                    "Забрать шнур.":
                        $ playerHasCabel = False
                        call take_item("cable")
                    "Уйти.":
                        pass
        else:
            if inventory.lastItem == "cable":
                $ playerHasCabel = True
                $ inventory.applyItem(inventory.lastItem)
            else:
                "Мафон без питания - музыку не послушать."
    elif obj == "server":
        player """
        Сервер работает - квартира обогревается.
        
        Пока всё логично.
        """

    window hide
    $ renpy.pause(hard=True)
    return