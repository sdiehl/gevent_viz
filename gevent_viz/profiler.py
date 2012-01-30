#!/usr/bin/env python
import argparse
import trace
import visualise

def run(args):
    module = args.action[1]
    trace.patch_greenlet(file(args.output,'w'))

    try:
        a = __import__(module)
    except ImportError:
        print 'Could not find module', module

def html(args):
    viz = visualise.Visualiser(file(args.output,'r'))
    viz.go()

def main():
    import os, sys
    os.path.join(os.getcwd())
    sys.path.append(os.getcwd())
    print os.getcwd()

    parser = argparse.ArgumentParser()
    parser.add_argument('action', metavar='action', type=str,
            nargs='*', help='Action.')

    parser.add_argument('--output', default=".gevent_profile",
            help='Profile file output.')
    args = parser.parse_args()

    if len(args.action) == 2  and args.action[0] == 'run' :
        run(args)
    elif len(args.action) == 1 and args.action[0] == 'html':
        html(args)
    else:
        print 'Unknown action: run <module> | html'

if __name__ == '__main__':
    main()
