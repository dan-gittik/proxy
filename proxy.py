from __future__ import print_function

import contextlib
import socket

import socks
import stem.process


default_proxy_host = '127.0.0.1'
default_proxy_port = 7000
default_tor_port   = 7000


@contextlib.contextmanager
def proxy(host=None, port=None):
    if host is None:
        host = default_proxy_host
    if port is None:
        port = default_proxy_port
    old_socket = socket.socket
    try:
        socks.set_default_proxy(socks.SOCKS5, host, port)
        socket.socket = socks.socksocket
        yield
    finally:
        socket.socket = old_socket


@contextlib.contextmanager
def tor_proxy(country, port=None):
    if port is None:
        port = default_tor_port
    tor_process = stem.process.launch_tor_with_config(
        config = {
            'SocksPort': str(port),
            'ExitNodes': '{%s}' % country,
        },
        init_msg_handler = print,
    )
    try:
        with proxy(host='127.0.0.1', port=port):
            yield
    finally:
        tor_process.kill()
