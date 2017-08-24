import sys
import os
import subprocess
import signal
from os.path import abspath, dirname, exists, join, normpath

CURDIR = dirname(abspath(__file__))
TEMPDIR = r'C:\Users\i067382\PycharmProjects\robotframework\mytest\temp'


def _run(args, tempdir):
    runner = normpath(join(CURDIR, '..', 'src', 'robot', 'run.py'))
    command = [sys.executable, runner] + args
    environ = dict(os.environ, TEMPDIR=tempdir)
    sys.stdout.flush()
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    return subprocess.call(command, env=environ)


if __name__ == '__main__':
    debugfile = r'C:\Users\i067382\PycharmProjects\robotframework\mytest\debug.log'
    args = ['--name', 'tcase01', '--debugfile', debugfile, 'testcase.robot']
    _run(args, TEMPDIR)
    # robot.run_cli(['--name', 'tcase01', '--debugfile', debugfile, 'testcase.robot'])
