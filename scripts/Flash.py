from scripts.set_accounts import *
from scripts.get_weth import *
from brownie import Flash

LOAN = 500000000000000000


def deployer(Aave, cta):
    contract = Flash.deploy(Aave, {'from': cta})
    print("Deployed.")
    return contract


def founding(asset, c, amount, cta):
    tx = asset.transfer(c.address, amount * 10**18, {'from': cta})
    tx.wait(1)
    print("Transaction finished.")
    print("New balance:", asset.balanceOf(c.address))


def main():
    user, aave, weth, wmatic, dai = setting_accounts()
    contract = deployer(aave, user)
    if network.show_active() == 'polyfork':
        getting_matic(user, wmatic, 50)
    founding(wmatic, contract, 1, user)
    print("*" * 100)
    if wmatic.balanceOf(contract.address) > 0:
        loan = contract.initFlashLoan(wmatic, LOAN, {'from': user})
        loan.wait(1)
    print(loan.info())
    wt = contract.withdraw(wmatic, {'from': user})
    wt.wait(1)
    print(wt.info())
    print("Contract balance", wmatic.balanceOf(contract.address))
    print("User balance:", wmatic.balanceOf(contract.owner()))
    print("ANIMENSE A PROCEDER")
