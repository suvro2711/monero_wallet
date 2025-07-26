# wallet_data Directory

This folder is used to store Monero wallet files, keys, and related data. By mounting this directory as a Docker volume, wallet data persists outside the container and remains safe even if the container is removed.

## Purpose
- Store wallet keys and files securely
- Enable persistent access to wallet data across container sessions
- Facilitate backup and recovery of wallet information

## Steps to Create and Use the Docker Container

1. **Build the Docker image:**
   ```powershell
   docker build -t monero_wallet .
   ```

2. **Run the container with a mounted volume:**
   ```powershell
   docker run --rm -it -v D:\Personal\monero_wallet\wallet_data:/wallet_data monero_wallet bash
   ```
   - This mounts the local `wallet_data` folder to `/wallet_data` inside the container.

3. **Create or manage wallet files inside the container:**
   - Save wallet files and keys in `/wallet_data` to ensure persistence.

4. **Stop and remove the container:**
   - The `--rm` flag ensures the container is removed after exit, but your wallet data remains in `wallet_data`.

## Notes
- Always back up your wallet files stored in this directory.
- Never share your private keys or mnemonic phrases.
- You can use this directory for both mainnet and testnet wallets.
