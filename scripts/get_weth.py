from brownie import interface


def getting_weth(user, weth, amount):
    weth.deposit({'from': user, 'value': amount * 10**18})
    print("Printer goes brrrrr")


def getting_matic(user, wmatic, amount):
    wmatic.deposit({'from': user, 'value': amount * 10**18})
    print("Printer goes brrrr MATICS ULTRACROCANTES")
