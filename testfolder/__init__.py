import sys
from testfolder.queryApi import queryApi
from testfolder.gifTerms import gifTerms

cliCmds = {
    "-q": queryApi,
    "-c": gifTerms
}

def init():
    argv = sys.argv
    if len(argv) == 1:
        cliCmds['-q'](argv)
    else:
        try:
            cliCmds[argv[1]](argv)
        except:
            print(f"Unknown flag: {argv[1]}")

if __name__ ==  '__main__':
    init()