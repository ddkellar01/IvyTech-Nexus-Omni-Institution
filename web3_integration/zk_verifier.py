import json
from web3 import Web3

class ZeroKnowledgeCurricularVerifier:
    def __init__(self, rpc_url: str, contract_address: str, abi: list):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract_address = Web3.to_checksum_address(contract_address)
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=abi)

    def verify_zk_proof(self, proof_hash: str, expected_commitment: str) -> bool:
        try:
            is_valid = self.contract.functions.verifyProof(proof_hash, expected_commitment).call()
            return bool(is_valid)
        except Exception as e:
            print(f"[!] ZK-Proof blockchain verification exception: {e}")
            return False
