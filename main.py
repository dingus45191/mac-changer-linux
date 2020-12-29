import subprocess

subprocess.call("ifconfig wifi0 down", shell=True)
subprocess.call("ifconfig wifi0 hw ether 00:11:22:33:44:77", shell=True)
subprocess.call("ifconfig wifi0 up", shell=True)
