Config proxy first if needed.

# Basic environment

Open `terminal.app`

Install dev tools:
```sh
xcode-select --install
```

Install home-brew:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install fish:
```
/opt/homebrew/bin/brew install fish
echo /opt/homebrew/bin/fish | sudo tee -a /etc/shells
chsh -s /opt/homebrew/bin/fish
```

Open a new fish shell session.

Add `/opt/homebrew/bin` to `$PATH`:
```sh
fish_add_path /opt/homebrew/bin
```

Install `warp` as terminal app (Avoid configuring the appearance of fish with omf):
```sh
brew install warp
```

Open warp.

If you agree with configs below, run `./auto-install.sh` directly.

# Compilers and interpreters

## Rust
```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
New a shell session:
```sh
# nightly rust
rustup toolchain install +nightly
# cargo tools
brew install cargo-binstall
cargo binstall cargo-cache cargo-watch
```

## Zig
```sh
brew install zig
```

## Python
`uv` does things on python like cargo on rust:
```sh
brew install uv
```

## js/ts
`bun` for its performance:
```sh
curl -fsSL https://bun.sh/install | bash
```

# Editor

## zed
```sh
brew install zed
```

## typora
```sh
brew install typora
```

# Virtualization tools

podman, kubectl, minikube:
```sh
brew install podman kubectl minikube qemu
```
wine (for play Windows games):
```sh
brew install wine-stable
```

# Microsoft things

Onedrive
```sh
brew install --cask onedrive
```

Word, excel and ppt:
```sh
brew install microsoft-word microsoft-powerpoint microsoft-excel
```

# media player
```sh
brew install iina neteasemusic
```

# command line tools

```sh
brew install tldr ripgrep zoxide zellij lsd fd ffmpeg

zellij setup --generate-completion fish >> ~/.config/fish/completions/zellij.fish
```

Add this to `~/.config/fish/config.fish`:
```fish
# lsd
alias ls='lsd'
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias lt='ls --tree'

# zellij
alias zel='zellij'

# zoxide
zoxide init fish | source
```

# other

Install `ipreview` in app store.

# More configuration to do

After install all things, here are more configuration to do.

## application login

These apps need login:
- onedrive
- neteasemusic
- zed (and GitHub copylot in it)

## application to activate

- typora

## ssh

ssh key for GitHub or other machine.
```sh
ssh-keygen
```

## editor configure

zed (see `zed-settings.json`)

vim (~/.vimrc)
```ini
set number
set tabstop=4
set shiftwidth=4
set expandtab
```

## git

Basic info:
```sh
git config --global user.name "..."
git config --global user.email "..."
```

Create gpg key following [github doc](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key)

```sh
gpg --full-generate-key
gpg --list-secret-keys --keyid-format=long
# ...
# sec   ed25519/XXX...XXX 2025-03-08 [SC]
# ...
gpg --armor --export XXX...XXX
```

Add **all** the output to the GitHub account.

Tell git which key to use:
```sh
# if configured before, unset first
git config --global --unset gpg.format

gpg --list-secret-keys --keyid-format=long
git config --global user.signingkey XXX...XXX
git config --global commit.gpgsign true
git config --global tag.gpgSign true
```

## Rust cargo
rust/.cargo/config.toml
```toml
[build]
target-dir = "target"
```

## macOS
Enable holding key to repeat (need relog in):
```sh
defaults write -g ApplePressAndHoldEnabled -bool false
```

# clean cache
Clean homebrew cache
```sh
brew update && brew upgrade && brew cleanup
brew autoremove
```

