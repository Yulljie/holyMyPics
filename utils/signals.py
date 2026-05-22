import signal
import sys

def sigint(signum, frame):
    print("收到 SIGINT，退出程序")
    sys.exit(0)

def reg_sig():
    print("注册 signal")
    signal.signal(signal.SIGINT, sigint)

