# pythoneda-sandbox/flow-sample

A Python project used to show a simple flow in PythonEDA.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-sandbox-def/flow-sample/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-sandbox-flow-sample = {
      [optional follows]
      url =
        "github:pythoneda-sandbox-def/flow-sample/[version]";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is managed by [https://github.com/pythoneda-sandbox-def/flow-sample](flow-sample "flow-sample") definition repository.

