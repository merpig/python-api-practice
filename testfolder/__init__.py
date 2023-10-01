import sys
from testfolder.queryApi import queryApi

cliCmds = {
    "-c": queryApi
}

def init():
    argv = sys.argv
    if len(argv) == 1:
        cliCmds['-c'](argv)
    else:
        cliCmds[argv[1]](argv)

if __name__ ==  '__main__':
    init()