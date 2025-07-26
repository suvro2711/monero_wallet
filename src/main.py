from key_manager import KeyManager
from address_generator import AddressGenerator

km = KeyManager()
ag = AddressGenerator(km.get_seed())

print("Main address:", ag.get_main_address())
print("Public keys:", ag.get_public_keys())
