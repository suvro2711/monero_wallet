from monero.wallet import Wallet
from monero.seed import Seed
from monero.account import Account

class KeyManager:
    def __init__(self):
        self.seed = Seed()
        self.private_spend_key = self.seed.secret_spend_key()
        self.private_view_key = self.seed.secret_view_key()
        self.public_spend_key = self.seed.public_spend_key()
        self.public_view_key = self.seed.public_view_key()
        self.address = self.seed.public_address()

    def get_seed(self):
        return self.seed
    
    def show_keys(self):
        return {
            "mnemonic": str(self.seed),
            "private_spend_key": str(self.private_spend_key),
            "private_view_key": str(self.private_view_key),
            "public_spend_key": str(self.public_spend_key),
            "public_view_key": str(self.public_view_key),
            "main_address": str(self.address)
        }

# Example usage
if __name__ == "__main__":
    km = KeyManager()
    for k, v in km.show_keys().items():
        print(f"{k}: {v}")
