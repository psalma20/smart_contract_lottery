# $50 =0.026
# 0.026 ETH =26000000000000000 wei
from brownie import Lottery,accounts,config,network
from web3 import Web3 
def test_get_entrance_fee():
    account=accounts.add(config["wallets"]["from_key"])
    lottery=Lottery.deploy(config["networks"] [network.show_active()] ["eth_usd_price_feed"] ,{"from":account})
    assert lottery.getEntranceFee() > Web3.toWei(0.18,"ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.029,"ether")

      