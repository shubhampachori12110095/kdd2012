import math


def zero(classes_count):
    return 0


def log_regularization(classes_count):
    total = 0
    for value in classes_count.values():
        total += value
    return -0.2 * math.log(1.0 * total / 200)