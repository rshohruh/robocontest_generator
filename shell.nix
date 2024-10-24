{ pkgs ? import <nixpkgs> { } }:
let
  getLibFolder = pkg: "${pkg}/lib";
in
pkgs.mkShell {
  name = "python-dev-shell";

  buildInputs = with pkgs; [
    gcc
    clang-tools
    python3
    nixd
    unzip
  ];

  shellHook = ''
    echo "Hello User, Welcome to test generator app
  '';
}
