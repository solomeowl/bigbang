from eth_account import Account
from web3 import Web3
import json
import secrets
from csv import DictWriter
import time
headersCSV = ['addr', 'priv', 'balance']
abi = ''
with open("./fetch.json") as f:
    abi = json.load(f)
web3 = Web3(Web3.HTTPProvider(
    'https://mainnet.infura.io/v3/改一下'))

contract_addr = Web3.toChecksumAddress(
    '0xE26357e976Fa720E8cb743Cc74b5C8E474382501')
contract = web3.eth.contract(address=contract_addr, abi=abi)
addrs = []
privates = []
while True:
    print("開始時間：", time.ctime(time.time()))
    for i in range(5000):
        priv = secrets.token_hex(32)
        private_key = "0x" + priv
        acct = Account.from_key(private_key)
        addrs.append(acct.address)
        privates.append(private_key)
    print("地址建立完成")
    balance = contract.functions.getBalance(addrs).call()
    print("合約查詢完成")
    for i in range(5000):
        if balance[i] > 0:
            print("找到大祕寶!地址為: ", addrs[i])
            print("找到大祕寶!私鑰為: ", privates[i])
            print("找到大祕寶!金額為: ", balance[i])
            with open('gold.csv', 'a', newline='') as f_object:
                dict = {'addr': addrs[i], 'priv': privates[i],
                        'balance': str(balance[i])}
                dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
                dictwriter_object.writerow(dict)
                f_object.close()
    print("結束時間：", time.ctime(time.time()))
    print("====================================")
