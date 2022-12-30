import colors_file as Color


class CarteSon:
    """Class carte son premet de repertorier les type de carte"""

    def __init__(self, channels: int = 0, wordclock: str = '', clockrtc: str = '', interface: str = ''):
        self.channels = channels
        self.wordclock = wordclock
        self.clockrtc = clockrtc
        self.interface = interface
        self.all = []
        self.set_all(self.channels, self.wordclock, self.clockrtc, self.interface)
        self.carte = "Carte RME"

    def set_specifications(self, schannels: int = 0, swordclock: str = '', sclockrtc: str = '', sinterface: str = ''):
        """Method set_specifications setter les valeures"""
        self.channels = schannels
        self.wordclock = swordclock
        self.clockrtc = sclockrtc
        self.interface = sinterface
        self.all.clear()
        self.all.append(self.channels)
        self.all.append(self.wordclock)
        self.all.append(self.clockrtc)
        self.all.append(self.interface)

    def get_channels(self, chan: int = 0):
        """Method get_channels recuperation de la valeur existante"""
        channels = 0
        for j in self.all:
            if chan == j:
                channels = j
        return channels

    def get_channels_str(self, chan: str = ''):
        """Method get_channels recuperation de la valeur existante"""
        channels = 0
        for j in self.all:
            if chan == j:
                channels = j
        return channels

    def set_channels(self, chanls: int = 0):
        """Method set_channels setter la nouvelle valeur pour channels"""
        getchannels = self.get_channels(self.channels)
        getindex = self.all.index(getchannels)
        self.all[getindex] = chanls
        self.show_carteson()

    def set_all(self, sch: int = 0, sw: str = '', sc: str = '', si: str = ''):
        """Method set_all setter toutes les valeures"""
        self.channels = sch
        self.wordclock = sw
        self.clockrtc = sc
        self.interface = si
        self.all.clear()
        self.all.append(self.channels)
        self.all.append(self.wordclock)
        self.all.append(self.clockrtc)
        self.all.append(self.interface)

    def set_swordclock(self, wclock: str = ''):
        """Method set_swordclock setter le wordclock"""
        getwordclock = self.get_channels_str(self.wordclock)
        getwordclockindex = self.all.index(getwordclock)
        self.all[getwordclockindex] = wclock

    def show_carteson(self):
        """Method show_carteson print des valeures"""
        print("---------- Details --------------")
        for j in self.all:
            print(j)
        print("---------------------------------")

    def show_carteson_modif(self):
        """Method show_carteson print des valeures avec modifs"""
        print("--------------- Details Modifs -----------------")
        for j in self.all:
            print(j)
        print("------------------------------------------------")


class CarteSonDetails(CarteSon):
    """Class CarteSonDetails de la carte son"""
    def __init__(self, sch: int = 0, sw: str = '', sc: str = '', si: str = ''):
        self.sch = sch
        self.sw = sw
        self.sc = sc
        self.si = si
        self.durec = ''
        # super().__init__(sch, sw, sc, si)  or bellow
        CarteSon.__init__(self, sch, sw, sc, si)

    def appelmethod(self):
        """Method appelmethod call self.durec value from parent"""
        self.durec = 'USB functionality'
        print("Appel de la fonction fils : ", self.durec)
        print("------------------------------------------------")

    def getcarte(self):
        """Method getcarte get value from self.carte from parent"""
        print("Carte Son : ", self.carte)


def getcarteson(carteson):
    """Method getcarteson the var carteson still waiting a class"""
    carteson.show_carteson_modif()
    carteson.carte = "Focusrite i2"
    print("Carte Son:", carteson.carte)


def getcarteson2(carteson):
    """Method getcarteson2 the var carteson still waiting a class
    and set a new value for carteson.carte"""
    nouvelle = carteson.carte = "Alesis 340p"
    return nouvelle


def getcarteson3():
    """Method getcarteson3 get all values and and create a new object type CarteSonDetails()"""
    version = int(input("Entrer la version (500,600) :"))
    mhz = str(input("Entrer les MHZ ('400 MHZ' or '600 MHZ') :"))
    dtc = str(input("Entrer DTC ou RTC ('Internal RTC' or 'External RTC') :"))
    console = str(input("Entrer DTC ou RTC ('Total Mix' or 'Alesis Mix') :"))
    carteson1 = CarteSonDetails(version, mhz, dtc, console)
    return carteson1


def getalldocs():
    print("-" * 48 + Color.bleu + " LIST OF METHOD AND CLASS DOCS " + Color.cend + "-" * 48)
    print('-' * 127)
    print('| \x1b[0;31;40m%-40s\x1b[0m| \x1b[0;31;40m%-20s\x1b[0m| '
          '\x1b[0;31;40m%-60s\x1b[0m|' % ("Class Name", "Class / Method", "Doc"))
    print('-' * 127)
    print('| %-40s| %-20s| %-60s|' % ("CarteSonDetails", "Class", CarteSonDetails.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("appelmethod", "Method", CarteSonDetails.appelmethod.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("getcarte", "Method", CarteSonDetails.getcarte.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("set_specifications", "Method", CarteSonDetails.set_specifications.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("CarteSon", "Class", CarteSon.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("get_channels", "Method", CarteSon.get_channels.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("get_channels_str", "Method", CarteSon.get_channels_str.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("set_channels", "Method", CarteSon.set_channels.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("set_all", "Method", CarteSon.set_all.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("set_swordclock", "Method", CarteSon.set_swordclock.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("show_carteson", "Method", CarteSon.show_carteson.__doc__))
    print('| %-40s| %-20s| %-60s|' % ("show_carteson_modif", "Method", CarteSon.show_carteson_modif.__doc__))
    print('-' * 127)
    print("-" * 56 + Color.bleu + " END OF LIST " + Color.cend + "-" * 56)


if __name__ == '__main__':
    crt = CarteSon(20, '400 MHZ', 'Internal RTC', 'TotalMix')
    crt.show_carteson()
    crt.set_channels(30)
    crt.set_all(50, '800 MHZ', 'Internal RTC', 'MixConsole')
    crt.show_carteson()
    crt.set_swordclock('1200 MHZ')
    crt.show_carteson_modif()

    crtfils = CarteSonDetails(80, '1400 MHZ', 'Local RTC', 'No Mix console')
    crtfils.show_carteson_modif()
    crtfils.appelmethod()
    crtfils.set_swordclock('2000 MHZ')
    crtfils.show_carteson_modif()
    crtfils.getcarte()
    ff = CarteSonDetails(100, '2500 MHZ', 'Local DTC', 'Mix console RME')
    getcarteson(ff)
    dd = CarteSonDetails(4400, '0.1 MHZ', 'DTC and RTC', 'Mix console Alesis')
    print(getcarteson2(dd))
    gg = getcarteson3()
    gg.show_carteson()
    getalldocs()
