from web3 import Web3

class AcademicGovernanceDAO:
    """Manages on-chain proposal voting for curriculum and model architecture updates by faculty nodes."""
    def __init__(self, rpc_url: str, dao_contract_address: str, abi: list):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract = self.w3.eth.contract(address=Web3.to_checksum_address(dao_contract_address), abi=abi)

    def cast_vote(self, proposal_id: int, support: bool, private_key: str) -> str:
        account = self.w3.eth.account.from_key(private_key)
        txn = self.contract.functions.vote(proposal_id, support).build_transaction({
            'from': account.address,
            'nonce': self.w3.eth.get_transaction_count(account.address),
            'gas': 200000,
            'gasPrice': self.w3.to_wei('10', 'gwei')
        })
        signed = self.w3.eth.account.sign_transaction(txn, private_key=private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed.rawTransaction)
        return tx_hash.hex()
