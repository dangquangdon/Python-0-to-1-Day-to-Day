def logger_file(func):
    import logging

    filename = "{}.log".format(func.__name__)

    logging.basicConfig(filename=filename,
                        level=logging.INFO)

    def wrapper(*args, **kwargs):
        info = "Ran with args: {}, and kwargs: {}".format(args, kwargs)
        logging.info(info)
        return func(*args, **kwargs)

    return wrapper


def timer(func):
    import time

    def wrapper_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()

        filename = func.__name__
        runtime = t2 - t1

        print("{} ran in {} sec".format(filename, runtime))

        return result

    return wrapper_func

import time

@timer
def sayHi(name, title):
    print("Hi there, {} - {}".format(name, title))

sayHi("Daniel", "The King")