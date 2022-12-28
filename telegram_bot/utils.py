from aiogram.utils.helper import Helper, HelperMode, ListItem


class StatesSaveProducts(Helper):
    mode = HelperMode.snake_case

    STATE_ADD_ONE = ListItem()
    STATE_ADD_MORE = ListItem()

    STATE_ADD_ONE_1 = ListItem()

