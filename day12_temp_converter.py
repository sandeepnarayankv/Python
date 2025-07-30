def c_to_f(celcius:float) -> float:
    return celcius*9/5 + 32

def c_to_k (celcius:float) -> float:
    return celcius + 273.15

def k_to_c (kelvin:float) -> float:
    return kelvin - 273.15

def f_to_c (farenheit : float) -> float:
    return (farenheit - 32) * 5/9

def f_to_k (farenheit: float) -> float:
    return c_to_k(f_to_c(farenheit=farenheit))


def k_to_f (kelvin: float) -> float:
    return c_to_f(k_to_c(kelvin=kelvin))


if __name__ == "__main__":

    print(c_to_f(10))

    print(f_to_c(50))

    print(f_to_k(50))

    print(k_to_f(283.15))
