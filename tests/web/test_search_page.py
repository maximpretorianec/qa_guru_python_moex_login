import allure

from pages.web.base_page import BasePage
from pages.web.search_page import SearchPage


STORY = 'Крот'


@allure.epic('Страница поиска')
class TestBasePage:

    @allure.story('Открыть страницу поиска')
    @allure.title('Страница поиска должна открываться')
    @allure.feature('Страница поиска')
    @allure.label('owner', 'qaguru')
    @allure.label('layer', 'web')
    @allure.tag('smoke', 'regress', 'web', 'normal')
    @allure.severity('normal')
    def test_open_search_page(self):
        base_page = BasePage()
        search_page = SearchPage()

        base_page.open_main_page()
        base_page.remove_advertisement()
        search_page.search_story(STORY)

        search_page.check_search_stories()
        search_page.check_tag_stories(STORY)

    @allure.story('Открыть страницу поиска')
    @allure.title('Фильтры, по тегам, должны быть видны и применяться')
    @allure.feature('Фильтрация поиска постов, по тегам')
    @allure.label('owner', 'qaguru')
    @allure.label('layer', 'web')
    @allure.tag('smoke', 'regress', 'web', 'normal')
    @allure.severity('normal')
    def test_search_page_by_filter_tags(self):
        type_filter = '[мое]'
        group_filter = 'stories-search__types-group'
        base_page = BasePage()
        search_page = SearchPage()

        base_page.open_main_page()
        base_page.remove_advertisement()

        search_page.search_story(STORY)
        search_page.open_types_filter_search(group_filter)
        search_page.select_type_filter_search(type_filter)

        search_page.check_tag_stories_by_scroll(STORY)
        search_page.check_tag_stories(type_filter)

    @allure.story('Открыть страницу поиска')
    @allure.title('Фильтры, по рейтингу, должны быть видны и применяться')
    @allure.feature('Фильтрация поиска постов, по рейтингу')
    @allure.label('owner', 'qaguru')
    @allure.label('layer', 'web')
    @allure.tag('smoke', 'regress', 'web', 'normal')
    @allure.severity('normal')
    def test_search_page_by_rating(self):
        group_filter = 'stories-search-rating'
        base_page = BasePage()
        search_page = SearchPage()

        base_page.open_main_page()
        base_page.remove_advertisement()

        search_page.search_story(STORY)
        search_page.open_types_filter_search(group_filter)
        search_page.change_rating_filter()

        search_page.is_story()

    @allure.story('Открыть страницу поиска')
    @allure.title('Сортировка результатов поиска')
    @allure.feature('Сортировка постов, сначала свежее')
    @allure.label('owner', 'qaguru')
    @allure.label('layer', 'web')
    @allure.tag('smoke', 'regress', 'web', 'normal')
    @allure.severity('normal')
    def test_sort_search_result(self):
        type_sort = 'FRESH'
        base_page = BasePage()
        search_page = SearchPage()

        base_page.open_main_page()
        base_page.remove_advertisement()

        search_page.search_story(STORY)
        search_page.sort_stories(type_sort)

        search_page.is_story()
