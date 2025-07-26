import json

class UnsignedTxImporter:
    def __init__(self, path):
        with open(path, "r") as f:
            self.tx_data = json.load(f)

    def get_tx_data(self):
        return self.tx_data  # raw data for signer
