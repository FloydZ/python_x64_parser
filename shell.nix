{ pkgs ? import <nixpkgs> {} }:
let
  my-python = pkgs.python38;
  python-with-my-packages = my-python.withPackages (p: with p; [
    #pygments
	antlr4-python3-runtime
	Opcodes
	pycca
	#pytest
	#pytest-benchmark
  ]);
in
pkgs.mkShell {
  buildInputs = [
    python-with-my-packages
	pkgs.python-language-server
	antlr4_9
  ];
  shellHook = ''
    PYTHONPATH=${python-with-my-packages}/${python-with-my-packages.sitePackages}
  '';
}
