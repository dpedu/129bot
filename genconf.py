#!/usr/bin/env python3
import os
import sys


timefmt = "%Y-%m-%d %H:%M:%S".replace("%", "%%")


def main(host, port):
    """
    Generate a circus conf to run all the plugins
    """
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    print("[circus]\ncheck_delay = 2\nwarmup_delay = 1\nloglevel = DEBUG\n")

    for plugin in os.listdir("plugins"):
        if any([plugin.startswith(x) for x in [".", "_"]]):
            continue
        name = plugin.split(".")[0]

        print("[watcher:{name}]\n"
              "cmd = ../../plugins/{plugin}\n"
              "args = -i {host} -p {port}\n"
              "working_dir = data/{name}\n"
              "numprocesses = 1\n"
              "copy_env = True\n"
              "stop_children = True\n"
              "stdout_stream.class = FileStream\n"
              "stdout_stream.filename = ./data/logs/{name}.log\n"
              "stdout_stream.time_format = {timefmt}\n"
              "stderr_stream.class = FileStream\n"
              "stderr_stream.filename = ./data/logs/{name}.log\n"
              "stderr_stream.time_format = {timefmt}\n"
              "respawn = True\n".format(host=host, port=port, name=name, plugin=plugin, timefmt=timefmt))

        os.makedirs("./data/{}".format(name), exist_ok=True)
    os.makedirs("./data/logs".format(name), exist_ok=True)


if __name__ == '__main__':
    try:
        host, port = sys.argv[1:]
    except ValueError:
        print("usage:", __file__, "host port")
        sys.exit(2)
    main(host, port)
