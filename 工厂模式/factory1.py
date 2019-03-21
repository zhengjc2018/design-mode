'''
    抽象工厂模式
'''
class PizzaIngredientFactory:

    def create_dough(self):
        print('normal dough used!!!!!')

    def create_sauce(self):
        print('normal sauce used!!!!!')

    def create_chesse(self):
        print('normal chesse used!!!!!')

    def create_veggies(self):
        print('normal veggies used!!!!!')

    def create_pepperoni(self):
        print('normal pepperoni used!!!!!')

    def create_clam(self):
        print('normal clam used!!!!!')


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self, _tp='thick'):
        if _tp == 'thick':
            Dough.thick_crust_dough()
        elif _tp == 'thin':
            Dough.thin_crust_dough()
        else:
            super().create_dough()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_clam(self, _tp):
        if _tp == 'frozen':
            Clams.frozen_clams()
        elif _tp == 'fresh':
            Clams.fresh_clams()
        else:
            super().create_clam()

class Dough:
    def thick_crust_dough():
        print('thick crust dough used!!!')

    def thin_crust_dough():
        print('thin crust dough used!!!')


class Clams:
    def frozen_clams():
        print('frozen clams used!!!!')

    def fresh_clams():
        print('fresh clams used!!!')


if __name__ == '__main__':
    a = NYPizzaIngredientFactory()
    a.create_dough('thick')
    a.create_sauce()
    a.create_chesse()
    a.create_veggies()
    a.create_pepperoni()
    a.create_clam()