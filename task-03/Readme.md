# Hello, World!

1. First step was to install ruby by using sudo dnf install ruby as im using fedora
2. I had already installed python before.
3. Next i installed node js using sudo dnf install nodejs and similarly i had installed elixir and ruby
4. Installing rust was very different it had its own unique script curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
5. I didnt have to install C and C++ as text editor geany was already installed into my fedora.
6. sudo dnf install ruby
7. sudo dnf install golang
8. sudo dnf install ghc
9.  sudo dnf install erlang
<br>
    sudo dnf install elixir 
<br>
    `as to run it needs the erlang runtime first`


# How the overall code works:
- Bascially there are two parts, one for the upper half of the diamond and other for the lower half after the middle of the diamond.
- In the top half the first loop starts from 1 and is incremented by 2 and the space is calculated by n-1/2 and is repeated and the stars are printed.
- When i increases the padding or spaces decrease
- In the bottom half which starts from n-2 and decreases i by 2 and the stars are printed with the calculated space
