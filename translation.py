class Translation(object):
    START_TEXT = """<b>Hello
Please Enter your Telegram Phone Number, to get the APP ID & API HASH from <a href="https://my.telegram.org/apps">Telegram</a></b>

<i>(note: the phone no. must include the country code and if something goes wrong stop the bot and send /start again.)</i>"""
    AFTER_RECVD_CODE_TEXT = """<b>Now enter the code you received:</b>

<b>/start at any stage to re-enter your details</b>"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "Something Went Wrong. failed to get app id."
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
