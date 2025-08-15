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

## Example: Generated Wallet Information

After creating a new wallet, you will see output similar to the following:

```
Generated new wallet: A2MoDAuT4oFWYeht4jyqUUeyHri7N5PEmMJwZchNLNYtKT9y6DbevHNgK6XGN7qPS5dnRq7LXCkDtDRLFLW11fbPJshy16g
View key: 0776db476e88f8ff86a584ff103f510e50bd5468809b5ba0a080b2e4b874b809
```

Your wallet has been generated!

- To start synchronizing with the daemon, use the `refresh` command.
- Use the `help` command to see a simplified list of available commands.
- Use `help all` to see all available commands.
- Use `help <command>` to see documentation for a specific command.
- Always use the `exit` command when closing `monero-wallet-cli` to save your session's state. Otherwise, you may need to synchronize your wallet again (your wallet keys are NOT at risk).

> **Important:**  
> The following 25 words can be used to recover access to your wallet.  
> Write them down and store them somewhere safe and secure.  
> Do **not** store them in your email or on file storage services outside of your immediate control.

```
boyfriend salads september emit possible adjust offend anvil
bypass gaze amply when knapsack twice farming saxophone
ointment speedy iris torch gained sighting puffin push possible
```
**********************************************************************