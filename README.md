# Comp

Automated setup of my machines using Ansible. Currently supports OSX.

## Usage

Machines can be configured one of two ways. `script/rsync` can rsync
this repo to a remote machine over ssh. Then run `script/configure`
over SSH. This method is for provisoning a new machine from an old one
(say over SSH). Otherwise the repository can be cloned to the target
machine and run `script/configure`.

## Installed Programs

- ssh-copy-id
- brew
- vagrant
- git
- ag
- hub
