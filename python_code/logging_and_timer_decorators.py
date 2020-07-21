
def logger_decorator(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran w/ args: {}; and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def timer_decorator(orig_func):
    import time

    def wrapper(*args, **kwargs):
        import time

        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = orig_func(*args, **kwargs)
            t2 = time.time() - t1
            print('{} ran in: {} sec'.format(orig_func.__name__, t2))
            return result

        return wrapper
        
#use via @logger_decorator or @timer_decorator
