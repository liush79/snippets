import threading


class WorkThread(object):
    def __init__(self):
        self.funcs = []
        self.threads = []

    def add(self, func, *param):
        self.funcs.append({'func': func, 'param': param})

    def start(self):
        for f in self.funcs:
            t = threading.Thread(target=f['func'], args=f['param'])
            self.threads.append(t)
            t.start()

    def wait_and_end(self):
        for t in self.threads:
            t.join()
        self.threads = []


# example
if __name__ == '__main__':
    import time

    def cb_non_param():
        print('non_param callback - start')
        time.sleep(5)
        print('non_param callback - end')

    def cb_one_param(param1):
        print('one_param callback - start (%s)' % param1)
        time.sleep(5)
        print('one_param callback - end')

    def cb_two_param(param1, param2):
        print('two_param callback - start (%s, %d)' % (param1, param2))
        time.sleep(5)
        print('two_param callback - end')

    wt = WorkThread()
    wt.add(cb_non_param)
    wt.add(cb_one_param, 'param_1')
    wt.add(cb_two_param, 'param_1', 999)
    wt.start()
    wt.wait_and_end()
    print('End main thread')
