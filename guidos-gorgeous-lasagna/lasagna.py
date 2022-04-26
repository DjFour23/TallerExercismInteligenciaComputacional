EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time: int):
    """
    Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time;
# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(num_layers: int):
    '''
    Return preparation time based on numbers of layers in the lasagna
    '''
    return PREPARATION_TIME * num_layers;
# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(num_layers: int, elapsed_time: int):
    '''
    Return elapsed cooking time
    '''
    return preparation_time_in_minutes(num_layers) + elapsed_time;