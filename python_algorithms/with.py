# CONTEXT MANAGERS - anywhere you have setup and teardown that get repeated in
# your code, you want a context manager to improve it, example:
f = open("data.txt")
try:
    data = f.read()
finally:
    f.close()

# open handles the try/finally for us
with open("data.txt") as f:
    data = f.read()

# how to use locks:
lock = threading.lock
with lock:
    print("Critical section 1")
    print("Critical section 2")


# FACTORING OUT TEMPORARY CONTEXTS
try:
    os.remove("somefile.tmp")
except ODError:
    pass

with ignored(OSError):
    os.remove("somefile.tmp")

# HOW IT'S MADE
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


# MAKING YOUR OWN CONTEXT MANAGERS
# In order to make an object compatible with the with statement, you need to
# implement __enter__() and __exit__() methods. For example, consider the
# following class, which provides a network connection:

from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("Already connected")
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


# The key feature of this class is that it represents a network connection, but it
# doesn’t actually do anything initially (e.g., it doesn’t establish a
# connection). Instead, the con‐ nection is established and closed using the with
# statement (essentially on demand). For example:

from functools import partial

conn = LazyConnection(("www.python.org", 80))  # Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b"GET /index.html HTTP/1.0\r\n")
    s.send(b"Host: www.python.org\r\n")
    s.send(b"\r\n")
    resp = b"".join(iter(partial(s.recv, 8192), b""))
    # conn.__exit__() executes: connection closed
