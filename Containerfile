FROM docker.io/archlinux:latest

WORKDIR /root

# Install yay
RUN pacman -S --needed --noconfirm git base-devel && git clone https://aur.archlinux.org/yay-bin.git && cd yay-bin && makepkg -si

COPY . .

RUN python ./auto-install.py
