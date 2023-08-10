from yandex_page import YandexPage

def test_search():
    # создается экземпляр класса YandexPage
    yandex_page = YandexPage()

    # открывается страница поиска Яндекса
    yandex_page.open_search_page()

    # проверяется, что поле поиска присутствует на странице
    assert yandex_page.is_search_field_present()

    # вводится поисковый запрос "Тензор"
    yandex_page.enter_search_query("Тензор")

    # проверяется, что таблица с подсказками присутствует на странице
    assert yandex_page.is_suggest_table_present()

    # нажимается клавиша Enter
    yandex_page.press_enter()

    # проверяется, что страница с результатами поиска присутствует
    assert yandex_page.is_search_results_page_present()

    # проверяется, что первая ссылка на странице результатов соответствует ожидаемой ссылке "https://tensor.ru/"
    assert yandex_page.compare_first_link("https://tensor.ru/")


def test_open_image_and_navigate():
    # создается экземпляр класса YandexPage
    yandex_page = YandexPage()

    # открывается страница поиска Яндекса
    yandex_page.open_search_page()

    # проверяется, что кнопка меню присутствует на странице
    assert yandex_page.is_menu_button_present()

    # открывается страница с изображениями
    yandex_page.open_images_page()

    # проверяется, что URL страницы соответствует ожидаемому значению
    assert yandex_page.verify_url("https://ya.ru/images/")

    # открывается первая категория изображений на странице
    name_of_category = yandex_page.open_first_category()

    # проверяется, что название открытой категории соответствует ожидаемому значению
    assert yandex_page.check_category_name(name_of_category)

    # открывается первое изображение в категории
    yandex_page.open_first_image()

    # получается источник изображения
    image_src = yandex_page.get_image_source()

    # проверяется, что изображение успешно открылось
    assert yandex_page.is_image_opened()

    # нажимается кнопка "Вперёд"
    yandex_page.click_button_forward()

    # проверяется, что изображение изменилось (открылось новое)
    assert not yandex_page.is_image_remained_the_same(image_src)

    # нажимается кнопка "Назад"
    yandex_page.click_button_back()

    # проверяется, что изображение успешно открылось
    assert yandex_page.is_image_opened()

    # проверяется, что изображение осталось неизменным (т.е. осталось то же самое изображение изначально открытым)
    assert yandex_page.is_image_remained_the_same(image_src)


def run_tests():
    test_search()
    test_open_image_and_navigate()


if __name__ == "__main__":
    run_tests()
