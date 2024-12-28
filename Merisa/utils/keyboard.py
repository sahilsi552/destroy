from pyrogram.types import InlineKeyboardButton as Ikb, InlineKeyboardMarkup as Ikm
from Merisa.utils import get_urls_from_text as is_url

def keyboard(buttons_list, row_width: int = 2):
    """
    Buttons builder, pass buttons in a list and it will
    return pyrogram.types.InlineKeyboardMarkup object.
    
    Example:
    keyboard([["click here", "https://google.com"]])
    If there's a URL, it will make a URL button; otherwise, a callback button.
    """
    buttons = []  # Initialize an empty list to hold rows of buttons
    row = []

    for i in buttons_list:
        button = (
            Ikb(text=str(i[0]), callback_data=str(i[1]))
            if not is_url(i[1])
            else Ikb(text=str(i[0]), url=str(i[1]))
        )
        row.append(button)

        # Check if we reached the specified row width
        if len(row) == row_width:
            buttons.append(row)  # Add completed row to buttons
            row = []  # Reset for the next row

    # Add any remaining buttons that didn't complete a full row
    if row:
        buttons.append(row)

    return Ikm(buttons)

def ikb(data: dict, row_width: int = 2):
    """
    Converts a dict to pyrogram buttons.
    
    Example:
    ikb({"click here": "this is callback data"})
    """
    return keyboard(data.items(), row_width=row_width)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def ikb2(rows=None, back=False, todo="start_back"):
    """
    rows = pass the rows
    back - if want to make back button
    todo - callback data of back button
    """
    if rows is None:
        rows = []
    lines = []
    try:
        for row in rows:
            line = []
            for button in row:
                btn_text = button.split(".")[1].capitalize()
                button = btn(btn_text, button)  # InlineKeyboardButton
                line.append(button)
            lines.append(line)
    except AttributeError:
        for row in rows:
            line = []
            for button in row:
                # Will make the kb which don't have "." in them
                button = btn(*button)
                line.append(button)
            lines.append(line)
    except TypeError:
        # make a code to handel that error
        line = []
        for button in rows:
            button = btn(*button)  # InlineKeyboardButton
            line.append(button)
        lines.append(line)
    if back:
        back_btn = [(btn("« Back", todo))]
        lines.append(back_btn)
    return InlineKeyboardMarkup(inline_keyboard=lines)


def btn(text, value, type="callback_data"):
    return InlineKeyboardButton(text, **{type: value})