# Run Monero Wallet Docker Container with wallet_data_testnet Mounted
sudo usermod -aG docker $USER
docker run -it -v $(pwd)/wallet_data_testnet:/wallet_data_testnet monero_wallet bash
