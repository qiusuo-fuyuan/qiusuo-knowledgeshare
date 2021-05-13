from threading import Thread
BasePea = type("BasePea", (Thread,), {})

a = 5
