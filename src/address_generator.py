from monero.seed import Seed

class AddressGenerator:
    def __init__(self, seed: Seed):
        self.seed = seed

    def get_main_address(self):
        return str(self.seed.public_address())

    def get_public_keys(self):
        return {
            "public_spend_key": str(self.seed.public_spend_key()),
            "public_view_key": str(self.seed.public_view_key()),
        }
