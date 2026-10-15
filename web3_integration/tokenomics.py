from web3 import Web3

class SwarmProfessorStaking:
    """Handles staking and reward distribution for professor nodes based on peer-review accuracy."""
    def __init__(self, rpc_url: str, staking_contract_address: str, abi: list):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract = self.w3.eth.contract(address=Web3.to_checksum_address(staking_contract_address), abi=abi)

    def get_staked_balance(self, professor_wallet: str) -> float:
        checksum_addr = Web3.to_checksum_address(professor_wallet)
        wei_balance = self.contract.functions.stakedBalance(checksum_addr).call()
        return float(self.w3.from_wei(wei_balance, 'ether'))
