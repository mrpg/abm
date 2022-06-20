class Production:
    def __init__(self, name, input_water, input_money, output_water, output_money):
        self.name = name
        self.input_water = input_water
        self.input_money = input_money
        self.output_water = output_water
        self.output_money = output_money

    def __repr__(self):
        return f"<Production:{self.name}|{self.input_water},{self.input_money},{self.output_water},{self.output_money}>"
