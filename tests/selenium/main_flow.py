import unittest

if __name__ == "__main__":
    # Automatické nalezení a spuštění všech testů ve všech modulech
    unittest.TextTestRunner().run(unittest.defaultTestLoader.discover('.', pattern='TS*.py'))
