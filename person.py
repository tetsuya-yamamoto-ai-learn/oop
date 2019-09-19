class Person:
    def __init__(self, name, age):   # argument：引数
        # self.name は インスタンス変数(プロパティ/Field/Attribute)という
        self.name = name
        self.age = age



def main():
    # Personクラスをインスタンス化して、そのインスタンスをbobと名付けた
    bob = Person(name='Bob', age=18)
    print(bob)
    print(bob.name)
    print(bob.age)

    # Personクラスをインスタンス化して、そのインスタンスをtomと名付ける
    tom = Person(name='Tom', age=30)
    print(tom)
    print(tom.name)
    print(tom.age)

if __name__ == '__main__':
    main()
