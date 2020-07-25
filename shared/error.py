async def handle_error(e, bar_err = "ERR", sleep = 60):
    print(e, file=sys.stderr)
    print(e)
    yield fmt("{}".format(bar_err), colors={'fg': 'white', 'bg': 'red'})
    await sleep(60)

