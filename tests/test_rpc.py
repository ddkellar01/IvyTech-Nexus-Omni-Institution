import os
from web3 import Web3
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Monad Network Details
# Testnet RPC: https://testnet-rpc.monad.xyz (Chain ID: 10143)
# Mainnet RPC: https://rpc.monad.xyz         (Chain ID: 143)
MONAD_RPC_URL = os.getenv("MONAD_RPC_URL", "https://testnet-rpc.monad.xyz")

print(f"Connecting to Monad RPC endpoint: {MONAD_RPC_URL}")
w3 = Web3(Web3.HTTPProvider(MONAD_RPC_URL))

if w3.is_connected():
    print("✅ Successfully connected to Monad!")
    try:
        chain_id = w3.eth.chain_id
        latest_block = w3.eth.block_number
        print(f"🔗 Network Chain ID : {chain_id}")
        print(f"📦 Latest Block      : {latest_block}")
        
        # Verify network type
        if chain_id == 10143:
            print("🚀 Connected to: Monad Testnet")
        elif chain_id == 143:
            print("🚀 Connected to: Monad Mainnet")
        else:
            print(f"⚠️ Connected to custom/unknown chain ID: {chain_id}")
            
    except Exception as e:
        print(f"❌ Error querying network data: {e}")
else:
    print("❌ Failed to connect to Monad endpoint. Verify network status and endpoint URL.")
