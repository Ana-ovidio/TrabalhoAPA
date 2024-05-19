import importlib

try:
    main = importlib.import_module("main")
    graph = importlib.import_module("graph")

except ImportError as e:
    print(e)
