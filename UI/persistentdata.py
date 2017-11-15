import pickle

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)

def save_variable(name, value):
    data[name] = value
    return

def load_variable(name):
    if name not in data:
        data[name] = 0
    return data[name]

#data["mama"] = 233
print(load_variable("mama"))


def save_on_exit():
    with open('data.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    

