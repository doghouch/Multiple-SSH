import os, sys

"""
  NOTE: This WILL NOT run without a command or server(s) specified.

  This program supports custom ports and users:

    user  @  your.hostname  :  port

  If you do not specify a user, the program will default to root. In other words,
  your.hostname:2222 will be parsed as root@your.hostname:2222.

  Likewise, if you do not specify a port, the program will default to port 22. In other
  words, your.hostname will be parsed as root@your.hostname:22.

  Valid "HOSTNAMES" include (non-exhaustive list):
    - root@your.hostname:22
    - user@your.hostname:22
    - root@your.hostname:8888
    - user@your.hostname:1234
    - your.hostname:22
    - your.hostname    
    - 192.168.1.1:5555

    etc. (you get the point!)

  This program does not include a complete array of error-catching; ie. using an invalid hostname
  could cause undesired effects (crashing).

  It was designed for personal use and is now open-source; feel free to raise any issues on GitHub
  or fork it for your own program.
"""

HOSTNAMES = ["your.hostname:2222", "some.hostname"]

def get_port(a):
  """
    Returns '22' by default (default SSH port = 22), returns anything after ':'
    if a custom port is specified.
  """
  if ":" in a:
    return a.split(":")[1]
  return "22"

def get_username(a):
  """
    Return 'root' by default; returns anything before '@' if a custom username
    is specified.
  """
  if "@" in a:
    return a.split("@")[0]
  return "root"

def get_hostname(a):
  """
    Returns the hostname ignoring the username and port specified.
  """
  final_host = a
  if "@" in final_host:
    final_host = final_host[1 + final_host.index("@"):]
  if ":" in final_host:
    final_host = final_host[:final_host.index(":")]
  return final_host

def send_cmd(cmd):
  """
    Sends command to HOSTNAMES.
  """
  if not len(HOSTNAMES) > 0:
    print(f"\033[0;37;41mFATAL ERROR: NO HOSTNAMES DEFINED\033[0m\n")
    os.system("tput init")
  elif cmd:
    for a in HOSTNAMES:
      print(f"\033[0;37;46m" + a + "\033[0m")
      os.system("tput init")
      os.system("ssh -q " + get_username(a) + "@" + get_hostname(a) + " -p" + get_port(a) + " " + cmd)
      print("")
  else:
    print(f"\033[0;37;41mFATAL ERROR: NO COMMAND SPECIFIED\033[0m\n")
    os.system("tput init")

send_cmd(" ".join(a for a in sys.argv[1:]))

