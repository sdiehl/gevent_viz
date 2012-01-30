import time
import traceback
from gevent import Greenlet

old_run = None
out = None

def patch_greenlet(_out):
    '''
    Patches eventlet so that GreenThread will output trace to a file
    when created and run.
    '''
    if hasattr(Greenlet, 'vpatched'):
        return
    Greenlet.vpatched = True

    global out
    out = _out

    global old_run
    old_run = Greenlet.run
    Greenlet.run = new_main

    global old_init
    old_init = Greenlet.__init__
    Greenlet.__init__ = new_init

def new_main(self, *args):
    '''
    Override for the main method for a GreenThread.
    '''
    global old_run
    _id = id(self)
    signature = (str(self), self.args)
    try:
        out.write('S\n%s\n%s\n%s\n' % (
            _id,
            time.time(),
            signature
        ))
        return old_run(self, *args)
    finally:
        out.write('E\n%s\n%s\n' % (
            _id,
            time.time(),
        ))
        out.flush()

def new_init(self, parent, *args, **kwargs):
    '''
    Overrides for the creation of a GreenThread.
    '''
    global old_init
    _id = id(self)
    stack = traceback.format_stack()
    out.write('C\n%s\n%s\n%s\n' % (
        _id,
        time.time(),
        stack,
    ))
    old_init(self, parent, *args, **kwargs)

