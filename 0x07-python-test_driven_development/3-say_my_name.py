"""This modole holds a function that prints a person's name

Example:
>>> say_my_name("Tunde", "Ade")
My name is Tunde Ade

"""


def say_my_name(first_name, last_name=""):
    """Prints a sentence with a person's name

    Parameters:
        first_name (str): the first name
        last_name (str): the last name

    Returns:
    void
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
