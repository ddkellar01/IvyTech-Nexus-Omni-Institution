from web3 import Web3

class AcademicCredentialNFT:
    """Manages the minting of decentralized academic degrees and peer-review badges on-chain."""
    def __init__(self, rpc_url: str, contract_address: str, abi: list, private_key: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract_address = Web3.to_checksum_address(contract_address)
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=abi)
        self.account = self.w3.eth.account.from_key(private_key)

    def mint_badge(self, recipient_address: str, token_uri: str) -> str:
        recipient = Web3.to_checksum_address(recipient_address)
        txn = self.contract.functions.mintBadge(recipient, token_uri).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 300000,
            'gasPrice': self.w3.to_wei('15', 'gwei')
        })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.account.key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.transactionHash.hex()
