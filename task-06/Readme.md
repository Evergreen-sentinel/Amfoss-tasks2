# OpenDocs

## amFOSS_daemon
### Overview

It is a simple discord bot which helps to keep track of the attendance of the club memebers using time-based scheduling based on data from an external API.
<br>
[Click-here](https://github.com/amfoss/amd) to go to the repository

### Setup Instruction:

1. **Clone the repository** 
    ```
    git clone https://github.com/amfoss/amd.git
2. **Installng rust, cargo and shuttle**
    ```
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    cargo add cargo-shuttle
3. **Checking if the versions are installed**
    ```
    cargo --version
4. **Installing the dependancies**
    :The dependacies are listed in the project file named Cargo.toml and to install it just use the command below in the terminal
    ```
    cargo build
5. **Before running the proramme**<br>
    You have to go to the discord developers website and create a new project and create a bot giving the necessary permissions in BOT section and then go to INSTALLATION and give permissions there and install the bot into your server using the link provided. After creating the bot copy the token and create a file (in this case secrets.toml) and give the token there according to the variable name (in this case DISCORD_TOKEN) 
6. **Running the file**
<br>Go to terminal and use the following command:
    ```
    cargo shuttle run

## Cargo:
Cargo is the package manager and build system for Rust. It handles downloading and managing the libraries (called crates) that your Rust project depends on, as well as compiling your code.

## Shuttle:
Shuttle is a platform for deploying Rust applications easily to the cloud. It simplifies the deployment process, allowing you to push your Rust project to a hosted environment with minimal setup.