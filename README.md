# MultipleSSH
## Introduction
An open-source program to perform SSH commands on multiple servers. It is (essentially) a "dumbed down" version of PSSH (parallel-ssh). 

## Use
This program has only been tested with Python 3.7+. Once you have that installed, open the Python file and edit the "HOSTNAMES" list to something like the following:

    HOSTNAMES = ["your.hostname:8888", "user@second-server.hostname"]

Once you've added your servers AND successfully enabled key authentication with those hostname(s), simply run the following to send a command:

    python send_cmd.py (command)

You should see:

    HOSTNAME_1:
     (response)

    HOSTNAME_2:
     (response)

# WARNING

Use of this program comes with no guarantees. If you have any suggestions, feel free to open an issue.


