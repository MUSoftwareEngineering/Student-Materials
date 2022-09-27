import Car

def test_wheels_on_car():
    mustang = Car.Car()
    mustang.setName("mustang")
    num_wheels = mustang.get_num_wheels()
    assert num_wheels == 4