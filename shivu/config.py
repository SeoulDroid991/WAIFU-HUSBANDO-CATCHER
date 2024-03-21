class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5746762799"
    sudo_users = "5746762799"
    GROUP_ID = -1002097725963
    TOKEN = "6453256066:AAE1Zcuk5udmu-73jLShBxmlXELrjqsev-k"
    mongo_url = "mongodb+srv://gokussj177171:yVXX8wbaD7pa1CTH@cluster0.h37d92k.mongodb.net/"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "-1002097725963"
    UPDATE_CHAT = "-1002097725963"
    BOT_USERNAME = "-1002097725963"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = 28213805
    api_hash = "8f80142dfef1a696bee7f6ab4f6ece34"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
