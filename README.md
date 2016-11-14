# Comp

Automated setup of my machines using Ansible. Currently supports OSX.
Supported Platforms:

* OSX

## OSX Configuration

* Homebrew with taps, casks, and standard brew packages
* The lovely [mas][] (with custom ansible modules, see `library`) for
  Mac App store automation.
* Secrets management via `security` CLI for OSX Keychain

**Manual Steps**

1. _possiblity_ do an initial login to the App Store.
1. Set all keys in OSX Keychain

## Usage

Machines can be configured one of two ways. `script/rsync` can rsync
this repo to a remote machine over ssh. Then run `script/configure`
over SSH. This method is for provisoning a new machine from an old one
(say over SSH). Otherwise the repository can be cloned to the target
machine and run `script/configure`. This will ask for the sudo
password upfront.

## Structure

This repository automates the setup of a new machine with as little
manual work as possible. At high level this means:

1. Installing software
1. Cloning my [dotfiles][]
1. Cloning my [bindir][]
1. Generating configuration for the machine to have all three work
   together.

Here's the file layout:

```
├── README.md
├── configure-minikube.yml      # Configure Minikube environments
├── configure-osx-dock.yml      # Arrange OSX Dock
├── configure-osx-packages.yml  # Install software for an OSX environment
├── configure-osx.yml           # Include all playbooks for OSX
├── configure-saltside.yml      # Setup Saltside (work) environment
├── configure-shell.yml         # Setup my shell
├── configure-ssh.yml           # Configure generic SSH settings
├── files
│   ├── env                     # Shell source file; intended by sourced in shell boot
│   └── saltside                # Role specific files
│       └── env.sh
├── group_vars
│   └── all.yml
├── library
│   ├── mas_app.py              # Ansible module for install Mac Store apps
│   ├── mas_login.py            # Ansible mobule to manage Mac Store login
│   ├── osx_dock.py             # Add/remove/order OSX Dock items
│   └── vagrant_plugin.py       # Add/remove vagrant plugins
├── lookup_plugins
│   └── secret.py               # Use secrets at provision time
└── script
    ├── configure               # Main script
    └── rsync                   # Util to rsync code to remote machine
```

Ansible playbooks do the bulk of the work. There are platform specific
playbooks (e.g. `foo-osx`) and non-platform specific playbooks. There
is a main playbook per platform (`configure-osx.yml`) that includes
all relevant playbooks. `script/configure` runs the whole process. It
bootstraps the particular platform (installs ansible and supporting
libraries) then runs platform's playbook.

The setup does not rely on secrets in code, rather it uses a custom
lookup plugin to read secrets from a store. Generated shell files use
the `comp-secret` command and subshells to export relevant environment
variables.

## Known Issues

* OSX Provisioning cannot run over SSH. `mas` fails when used over
  SSH. Also you must confirm key chain access in the GUI.

## Forking & Customizing

This code is primarily designed for my structure but it's keep
somewhat extensible to least support different platforms. You can fork
this repo for your own setup. If you do, you'll want to customize:

* `script/bootstrap` to add support for your platform (based on
  `uname -a`
* Create your own `comp-secret` to read secrets for your shell.
* If you _don't_ use fish, then update the generated shell files for
  your shell
* Update the keyring configuration for the lookup plugin to support
  your secret store _or_ swap for your own implementation.

[dotfiles]: https://github.com/ahawkins/dotfiles
[bindir]: https://github.com/ahawkins/bindir
[mas]: https://github.com/mas-cli/mas
