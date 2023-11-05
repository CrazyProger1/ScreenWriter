from src.core import Core
from src.context import Context

if __name__ == '__main__':
    context = Context()
    core = Core(context=context)
    core.run()
