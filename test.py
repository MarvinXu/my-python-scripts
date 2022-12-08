def run():
    try:
        print(0)
        raise Exception(1)
        print(2)
    except Exception as e:
        print(f"error: {e}")
        return

    try:
        print(3)
    except:
        pass


run()
