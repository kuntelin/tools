#!/usr/bin/env python

import os
import time
import datetime
import subprocess


def command_with_timeout(command, timeout=30):
    proc = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    start = datetime.datetime.now()
    while proc.poll() is not None:
        if (datetime.datetime.now() - start).seconds > timeout:
            proc.kill()

            raise Exception("Timeout")

        time.sleep(1)

    return proc.communicate()

if __name__ == "__main__":
    print command_with_timeout(raw_input("Enter command: "))

