init:
    # Выключение возможности прокрутки назад
    # В этой игре прокрутка назад не изменяет значение переменных в прошлое значение
    # Поэтому прокрутку отключить необходимо
    $ config.rollback_enabled = False
    # Определение видов курсоров с указанием использоуемого изображения
    $ config.mouse = {
        "default" : [ ("images/mouse/mouse_arrow.png", 0, 0) ],
        "search" : [ ("images/mouse/mouse_lupa.png", 19, 19) ],
        "put" : [ ("images/mouse/mouse_hand.png", 0, 0) ]
    }
    # Определение автоматического воспроизведения реплик персонажей
    define config.auto_voice = "voice/{id}.mp3"

    # Флаги и переменные для логики игры
    $ drinkWater = False
    $ computerCable = False
    $ seeCat = False
    $ takeCatFood = False
    $ putKey = False
    $ putCatFood = False
    $ hasKeyFridge = False
    $ openFridge = False
    $ playerOn = False
    $ playerHasCabel = True
    
    $ musicTrack = 0

    # Инициализация персонажей
    define player = Character('Петруха', color="#c8ffc8")

    # Инициализация изображений и фонов
    image start_image = "images/bg/start.png"
    image page_1 = "images/letters/page1.png"
    image black = "#000"
    
    image sleeping = "images/poster/sleeping.png"
    image finaly_end = "images/poster/final.png"
