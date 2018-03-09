import os
from file import Directory
from tempfile import TemporaryDirectory


class InputData(object):
    def read(self):
        raise NotImplementedError


class PathInputData(object):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    return [LineCountWorker(input_data) for input_data in input_list]


def execute(workers):
    threads = [Thread(target=w.map)
               for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, rest = workers[0], worker[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    for i in inputs:
        print(i)
    print(*inputs)
    # workers = create_workers(inputs)
    # return execute(workers)


def write_test_files(tmpdir):
    with open('foo', 'a') as out:
        out.write(f'blah\n')
    with open('boo', 'a') as out:
        out.write(f'blah\n')


with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    result = mapreduce(tmpdir)

print(f'There are {result} lines')
