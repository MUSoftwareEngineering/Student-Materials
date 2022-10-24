class Vehicle():

    def setName(self,name):
        self.name = name

    def get_name(self):
        return self.name


class Car (Vehicle):

    wheels = 4

    def get_num_wheels(self):
        return self.wheels


if __name__ == "__main__":
    mustang = Car()
    mustang.setName("mustang")
    print(mustang.get_name())
    print(mustang.get_num_wheels())
