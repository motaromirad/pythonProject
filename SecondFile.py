from main import print_hi

import os
import pickle

if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi('PyCharm2')
    a = 'blah blah blah'


    cwd=os.getcwd()
    print(cwd)
    with open(os.path.join(cwd, 'testfile'), 'wb') as handle:
        pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

    del a

    with open(os.path.join(cwd, 'testfile'), 'rb') as handle:
        b = pickle.load(handle)

    print(b)