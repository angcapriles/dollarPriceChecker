import rumps
import DollarRequest
import locale

class DollarChecker(rumps.App):
    def __init__(self):
        super(DollarChecker, self).__init__("DollarPrice")
        self.menu = ["Querying API..."]
        locale.setlocale(locale.LC_ALL, '')
    @rumps.timer(60)
    def showPrice(self, sender):
        _api = DollarRequest.fetchDolarPrice()
        self.title = "USD: " + str(locale.currency(_api['price'], grouping=True))

if __name__ == "__main__":
    DollarChecker().run()
