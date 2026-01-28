import inspect

def evolving():
    print("I am version 2.")

source = inspect.getsource(evolving)

if "version 2" not in source:
    new_source = source.replace("version 1", "version 2")

    with open(__file__, "r") as f:
        full_code = f.read()

    full_code = full_code.replace(source, new_source)

    with open(__file__, "w") as f:
        f.write(full_code)

evolving()
