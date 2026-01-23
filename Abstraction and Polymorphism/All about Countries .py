class Pakistan:
    def Capital(self):
        print("Pakistan's Capital Is Islamabad")
    def Language(self):
        print("Urdu is the language of Pakistan")
    def Type(self):
        print("Pakistan is developing country")
class USA:
    def Capital(self):
        print("USA'S Capital Is Washington D.C.")
    def Language(self):
        print("English is the language of USA")
    def Type(self):
        print("USA is developed country")
Pakistanobj = Pakistan()
USAobj = USA()
for country in(USAobj, Pakistanobj):
    country.Capital()
    country.Language()
    country.Type()