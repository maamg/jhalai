"""
Program: Weight on Planets
--------------------
This program calculates the weight of an object on different planets in our solar system.

The user is prompted to enter a weight on Earth and select a planet from Mercury, Venus, Mars, Jupiter, Saturn, Uranus, or Neptune. The program then calculates the equivalent weight of the object on the chosen planet, taking into account the gravity of that planet compared to Earth's gravity.

Note: The program assumes a standard gravitational pull on Earth and uses approximate gravity values for the other planets.

"""


def main():
    weight = float(input("Enter a weight on Earth: "))
    planet = input("Which planet do you want to test on? Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune: ").title()
    weight_on_planet(weight, planet)


def weight_on_planet(weight_on_earth, planet_name):
    """
    Calculate the weight of an object on a specific planet.

    Parameters:
    weight_on_earth (float): The weight of the object on Earth.
    planet_name (str): The name of the planet to calculate the weight on.

    Returns:
    float: The equivalent weight of the object on the specified planet.

    Raises:
    ValueError: If an invalid planet name is provided.

    """
    # Adjust Gravity of the planet compare to the earth
    if planet_name == 'Mercury':
        gravity = 37.6
    elif planet_name == 'Venus':
        gravity = 88.9
    elif planet_name == 'Mars':
        gravity = 37.8
    elif planet_name == 'Jupiter':
        gravity = 236.0
    elif planet_name == 'Saturn':
        gravity = 108, 1
    elif planet_name == 'Uranus':
        gravity = 81.5
    elif planet_name == 'Neptune':
        gravity = 114.0
    else:
        print("This planet is out of our solar-system")

    planet_weight = round(weight_on_earth * (gravity/100), 2)
    print(f"The equivalent weight on {planet_name}: {planet_weight}")


if __name__ == "__main__":
    main()

