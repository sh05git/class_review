class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.family_name

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif self.age >= 65:
            return 1200
        elif self.age >= 75:
            return 500

    def info_csv(self):
        return self.full_name() + "," + str(self.age) + "," + str(self.entry_fee())

    def info_csv_tab(self):
        return self.full_name() + "    " + str(self.age) + "    " + str(self.entry_fee())

    def info_csv_pipe(self):
        return self.full_name() + "|" + str(self.age) + "|" + str(self.entry_fee())


ken = Customer("Ken", "Tanaka", 15)
ken.full_name()
print(ken.full_name())
print(ken.age)
print(ken.entry_fee())
print(ken.info_csv())
print(ken.info_csv_tab())
print(ken.info_csv_pipe())

tom = Customer("Tom", "Ford", 57)
tom.full_name()
print(tom.full_name())
print(tom.age)
print(tom.entry_fee())
print(tom.info_csv())
print(tom.info_csv_tab())
print(tom.info_csv_pipe())

ieyasu = Customer("Ieyasu", "Tokugawa", 73)
ieyasu.full_name()
print(ieyasu.full_name())
print(ieyasu.age)
print(ieyasu.entry_fee())
print(ieyasu.info_csv())
print(ieyasu.info_csv_tab())
print(ieyasu.info_csv_pipe())
