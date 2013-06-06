import sys
from lust import log
from . import Service, Carbon
from tornado.ioloop import IOLoop

if __name__ == "__main__":
    if '--debug' in sys.argv:
        server =Carbon()
        server.listen(2003)
        IOLoop.instance().start()

    else:
        log.setup('/tmp/carbon.log')
        server = Service()
        server.run(sys.argv)
