from web3 import Web3

class FacultyReputationOracle:
    """Tracks and updates on-chain reputation scores for professor nodes based on peer-review accuracy."""
    def __init__(self, rpc_url: str, contract_address: str, abi: list):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract = self.w3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=abi)

    def fetch_professor_reputation(self, professor_wallet: str) -> int:
        checksum_addr = Web3.to_checksum_address(professor_wallet)
        score = self.contract.functions.getReputationScore(checksum_addr).call()
        return int(score)
