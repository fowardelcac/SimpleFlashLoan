from brownie import interface, config, accounts, network


def addresses(asset):
    return config['networks'][network.show_active()][asset]


def user_address():
    if network.show_active() == ('polyfork' or 'forky'):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def setting_accounts():
    user = user_address()
    aave = addresses('aave')
    weth = interface.WethInterface(addresses('weth'))
    wmatic = interface.WMATIC(addresses('wmatic'))
    dai = interface.IERC20(addresses('dai'))
    print("All too well.")
    return user, aave, weth, wmatic, dai


def just_deploy():
    user = user_address()
    aave = addresses('aave')
    print("I bet you think about me")
    return user, aave


def using():
    user = user_address()
    weth = interface.WethInterface(addresses('weth'))
    wmatic = interface.WMATIC(addresses('wmatic'))
    dai = interface.IERC20(addresses('dai'))
    print("All too well.")
    return user, weth, wmatic, dai
