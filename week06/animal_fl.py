#!/usr/bin/env python3
'''
在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。
这个类可以使用如下形式为动物园增加一只猫：

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
具体要求：
1、定义 动物、猫、狗、动物园 四个类，动物类不允许被实例化。
2、动物类要求定义 类型、体型、性格、是否属于凶猛动物 四个属性，是否属于凶猛动物的判断标准是：体型 >= 中等 并且是 食肉类型 同时 性格凶猛。
3、猫类要求有 叫声、是否适合作为宠物 以及 名字 三个属性，其中 叫声 作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
4、动物园类要求有 名字 属性和 添加动物 的方法，添加动物 方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
'''

class Animal(object):
    def __init__(self, aml_type, aml_shape, aml_character):
        self.aml_type = aml_type            # 类型
        self.aml_shape = aml_shape          # 体型
        self.aml_character = aml_character  # 性格 
    @property
    def is_tertible(self):
        figure_list = ['中等', '大型']
        if self.aml_shape in figure_list and self.aml_type == '食肉'  and self.aml_character == '凶猛':
            print('该动物为凶猛动物')
            return True
        else:
            print('该动物不是凶猛动物')
            return False
        
        
class Cat(Animal):
    sound = 'miaomiaomiaomiao'
    def __init__(self, name, aml_type, aml_shape, aml_character):
        self.name = name
        super().__init__(aml_type, aml_shape, aml_character) #通过super().__init__()继承父类的__init__；
    def is_pet(self):
        if not self.is_tertible:
            return True
        else:
            return False
    

class Dog(Animal):
    sound = 'wangwangwangwang'
    def __init__(self, name, aml_type, aml_shape, aml_character):
        self.name = name
        super().__init__(aml_type, aml_shape, aml_character)
    def is_pet(self):
        if not self.is_tertible:
            return True
        else:
            return False
        
    
class Zoo(object):
    def __init__(self, name):
        self.name = name 
        self.zname = []
        print(f'动物园的名称为{self.name}')
    def add_animal(self, aml):
        if aml.name not in self.zname:
            self.zname.append(aml.name)
            print(self.zname)
        else:
            print('该动物已存在.')
    
    # 通过__getattr__方法查询self.zname中是否存在对应的item；
    def __getattr__(self, aml):
        if aml in self.zname:
            print('存在该动物')
        else:
            print('不存在该动物')
            
            
if __name__ == '__main__':
    z = Zoo('时间动物园')
    
    cat1 = Cat('大花猫1', '食肉', '小', '温顺')
    print(cat1.is_pet())
    z.add_animal(cat1)
    
    dog1 = Dog('小狗', '食肉', '小', '温顺')
    print(dog1.is_pet())
    z.add_animal(dog1)
    
    dog2 = Dog('大狼狗', '食肉', '大型', '凶猛')
    print(dog2.is_pet())
    z.add_animal(dog2)
    
    have_cat = hasattr(z, 'Cat')
    print(have_cat)