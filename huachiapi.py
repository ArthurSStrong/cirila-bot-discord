from lib.instascrapper import Instascrapper

class Huachiapi:

    description = "description"
    default_msg = "Holis aún estoy bajo construcción!"

    def __init__(self):
        pass

    # Instance method
    def saldazo(self, *args):
        return f"{self.default_msg}"

    # Another instance method
    def shop(self, *args):
        if args[0] == 'frase_piolinera':
            i = Instascrapper("https://www.instagram.com/explore/tags/frasesdeldia/")
            reponse = i.get_photo()
            if reponse:
                return response
            else:
                return f"{self.default_msg}"

        else:
            return f"{self.default_msg}"

    # Another instance method
    def tip(self, *args):
        return f"<:huachi:809238593696432200>"
