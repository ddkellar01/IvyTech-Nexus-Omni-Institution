import os
from web3 import Web3

class SmartContractDeployer:
    def __init__(self, rpc_url: str, private_key: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = self.w3.eth.account.from_key(private_key)

    def deploy_contract(self, abi: list, bytecode: str, constructor_args: tuple) -> str:
        contract = self.w3.eth.contract(abi=abi, bytecode=bytecode)
        construct_txn = contract.constructor(*constructor_args).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 2000000,
            'gasPrice': self.w3.to_wei('20', 'gwei')
        })
        signed_txn = self.w3.eth.account.sign_transaction(construct_txn, private_key=self.account.key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.contractAddress
