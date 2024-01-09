import time

from selene import browser, be
from allure import step


SCROLL_PAUSE_TIME = 0.5


class SearchPage:
    def search_story(self, story):
        self.click_on_search()
        self.fill_search_string_stories(story)
        self.launch_search_stories()

    def click_on_search(self):
        with step('Нажать на кнопку поиска'):
            browser.element('[action="/search"]').should(be.visible).click()

    def fill_search_string_stories(self, story):
        with step('Заполнить поле поиска и запустить поиск'):
            browser.element('[placeholder="Поиск"]').type(story).wait_until('.dropdown-list__items')

    def launch_search_stories(self):
        with step('Заполнить поле поиска и запустить поиск'):
            browser.element('[placeholder="Поиск"]').press_enter()

    def check_search_stories(self):
        with step('Результаты поиска отображаются'):
            browser.element('div.stories-search-results')

    def check_tag_stories(self, story):
        with step('Искомый тег отображается'):
            browser.element(f'article [alt*="{story}"]').wait_until(be.visible)

    def open_types_filter_search(self,  group_filters):
        with step('Раскрыть фильтр по типу постов'):
            browser.element(f'.{group_filters}').should(be.visible).click()

    def select_type_filter_search(self, type_filter):
        with step('Выбрать фильтр по типу постов'):
            locator = f'//span[text()="{type_filter}"]'
            browser.element(f'//span[text()="{type_filter}"]').should(be.visible).click()

    def scroll_page(self, height = 'document.body.scrollHeight'):
        with step('Промотка страницы вниз'):
            browser.driver.execute_script(f"window.scrollTo(0, {height});")
            time.sleep(SCROLL_PAUSE_TIME)

    def get_height(self):
        return browser.driver.execute_script("return document.body.scrollHeight")

    def check_tag_stories_by_scroll(self, story):
        last_height = self.get_height()
        while not self.check_tag_stories(story):
            self.scroll_page()
            new_height = self.get_height()
            if new_height == last_height:
                with step('Конец страницы'):
                    break
            last_height = new_height

    def change_rating_filter(self):
        with step('Изменение рейтинга по фильтру'):
            browser.element('.slider').should(be.visible).click()

    def is_story(self):
        with step('Отображение постов'):
            browser.element('article.story').should(be.visible)

    def sort_stories(self, type_sort):
        with step('Сортировка постов'):
            browser.element('.stories-search__feed-panel a span').should(be.visible).click()
            browser.element(f'//input[@value="{type_sort}"]/ancestor::label').should(be.visible).click()
