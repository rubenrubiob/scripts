Set shell = CreateObject("WScript.Shell")
shell.Run "mstsc.exe /multimon c:remote.rdp", 1, True
shell.Run "shutdown -t 0 -s -f"