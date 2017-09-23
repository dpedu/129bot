#!/usr/bin/env python3

from _common import get_args
from contextlib import closing
from msgbus.client import MsgbusSubClient
from json import dumps, loads


def main():
    args = get_args()
    with closing(MsgbusSubClient(args.host, args.port)) as client:
        client.sub("pyircbot_command_ping")  # subscribe to .ping commnad
        while True:
            channel, msg = client.recv()
            _, rest = msg.split(" ", 1)
            channel, sender, trailing, extras = loads(rest)
            channel = channel[0]
            if not channel[0] == "#":
                # ignore PMs
                continue
            print("Pong: {} in {}".format(sender, channel))
            client.pub("pyircbot_send", "default privmsg {}".format(dumps([channel, "{}: pong".format(sender)])))


if __name__ == '__main__':
    main()
