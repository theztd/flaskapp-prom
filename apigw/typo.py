#!/usr/bin/env python3


def ret_string(name: str) -> str:
    print(type(name))
    return f"Hi {name}"


for n in ["Karel", "Pepa", 18, "Lucie"]:
    try:
        print(type(n))
        print(ret_string(n))
    except TypeError as err:
        print(n)
        print(err)
