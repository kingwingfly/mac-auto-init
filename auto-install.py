import logging
import os

PKG_MANAGER = {
    "linux": "yay -S --noconfirm",
    "darwin": "brew install",
    "cargo": "cargo binstall",
}


class Command:
    def __init__(self, cmd: str, info: str) -> None:
        self.cmd = cmd
        self.info = info

    def run(self) -> str:
        logging.info(f"Running: {self.cmd}")
        if not os.system(f"{self.cmd}"):
            return f"Success: {self.info}"
        return f"Failed: {self.info}; Command: {self.cmd}"


CURL_AND_BASH = {
    "rust toolchain": "https://sh.rustup.rs",
    "bun": "https://bun.sh/install",
}


PKG_INSTALL = {
    "cargo-binstall": "cargo-binstall",
    "zig": "zig",
    "python": "uv ruff",
    "zed": "zed",
    "zeditor": "zeditor",
    "typora": "typora",
    "virtualization": "podman kubectl minikube qemu wine-stable",
    "onedrive": "--cask onedrive",
    "microsoft": "microsoft-word microsoft-powerpoint microsoft-excel",
    "media": "iina neteasemusic",
    "command line tools": "tldr ripgrep zoxide zellij lsd fd ffmpeg",
    "obs": "obs",
}

CARGO_INSTALL = {"cargo tools": "cargo-cache cargo-watch"}


DIRECTLY_RUN = {
    "zellij init": "zellij setup --generate-completion fish >> ~/.config/fish/completions/zellij.fish",
    "zed config": "zed-settings.json ~/.config/zed/settings.json",
    "nightly rust": "rustup toolchain install nightly",
}

APPEND = {
    "~/.config/fish/config.fish": """
# lsd
alias ls='lsd'
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias lt='ls --tree'

# zellij
alias zel='zellij'

# zoxide
zoxide init fish | source""",
    "~/.vimrc": """
set number
set tabstop=4
set shiftwidth=4
set expandtab""",
}


def main():
    platform = os.uname().sysname.lower()
    for info, args in CURL_AND_BASH.items():
        logging.info(Command(f"curl {args} | bash", info).run())

    for info, args in PKG_INSTALL.items():
        logging.info(Command(f"{PKG_MANAGER[platform]} {args}", info).run())

    for info, args in CARGO_INSTALL.items():
        logging.info(Command(f"{PKG_MANAGER['cargo']} {args}", info).run())

    for info, args in DIRECTLY_RUN.items():
        logging.info(Command(f"{info}", info).run())

    for path, content in APPEND.items():
        with open(path, "a") as f:
            f.write(f"\n{content}\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
