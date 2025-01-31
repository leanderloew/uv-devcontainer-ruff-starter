from dependencies import HelloWorld


def hello_world() -> HelloWorld:
    return HelloWorld.HELLO_WORLD


if __name__ == "__main__":
    a = 1
    print(hello_world())
