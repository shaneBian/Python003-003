# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

#动物园
class  Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            self.__dict__[animal.__class__.__name__] = True

#动物
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, animal_type, body_size, nature):
        self.animal_type = animal_type
        self.body_size = body_size
        self.nature = nature

    @property
    def savage(self):
        if self.body_size != '小' and self.animal_type == '食肉':
            return True
        return False



#狗
class Dog(Animal):
    #叫声
    _sound = 'wangwang~'

    def __init__(self, name, animal_type, body_size, nature):
        self.name = name
        super().__init__(animal_type, body_size, nature)


    @property
    def pet(self):
        if self.savage == True:
            return False
        return True

#猫
class Cat(Animal):
    #叫声
    _sound = 'miaowu~'

    def __init__(self, name, animal_type, body_size, nature):
        self.name = name
        super().__init__(animal_type, body_size, nature)


    @property
    def pet(self):
        if self.savage == True:
            return False
        return True
    



if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    print(f'cat1是否为凶猛动物：{cat1.savage}')
    print(cat1.__dict__)
    cat2 = Cat('大花猫 2', '食肉', '大', '温顺')
    print(cat2.__dict__)
    print(f'cat2是否为凶猛动物：{cat2.savage}')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    print(z.__dict__)
    z.add_animal(cat1)
    print(z.__dict__)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)