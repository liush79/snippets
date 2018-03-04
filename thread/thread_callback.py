import threading


class CallbackThread(threading.Thread):
    def __init__(self, target, target_args=None,
                 callback=None, callback_args=None, *args, **kwargs):
        super(CallbackThread, self).__init__(target=self.target_wrapper, *args, **kwargs)
        self.target_method = target
        self.callback = callback
        self.callback_args = callback_args
        self.target_args = target_args

    def target_wrapper(self):
        self.target_method(*self.target_args)
        if self.callback:
            self.callback(*self.callback_args)


# example
if __name__ == '__main__':
    import time

    def my_work(param1, param2):
        print("Do my work - start ({}, {})".format(param1, param2))
        for i in range(1, 6):
            print('Working.. %d/5' % i)
            time.sleep(1)
        print("Do my work - end")

    def my_callback(param1, param2):
        print("My callback is called ({}, {})".format(param1, param2))


    thread = CallbackThread(target=my_work,
                            target_args=('target', 12345),
                            callback=my_callback,
                            callback_args=('callback', 67890))

    thread.start()
