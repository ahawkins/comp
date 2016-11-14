#!/usr/bin/env python

from ansible.module_utils.basic import *

def vagrant_plugin_present(module, args):
    name = args['name']

    list_rc, list_stdout, list_stderr = module.run_command([ 'vagrant', 'plugin', 'list' ], check_rc=True)

    if list_stdout.find(name) == -1:
        install_rc, install_stdout, install_stderr = module.run_command([ 'vagrant', 'plugin', 'install', name ], check_rc=True)
        return False, True, install_stdout
    else:
        return False, False, list_stdout

def main():
    fields = {
        "name": { "required": True, "type": "str" },
        "state": {
            "default": "present",
            "choices": [ 'present' ],
            "type": 'str'
        },
    }
    choice_map = {
        "present": vagrant_plugin_present
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, message = choice_map.get(module.params['state'])(module, module.params)

    if is_error:
        module.fail_json(msg=message)
    else:
        module.exit_json(changed=has_changed, stdout=message)

if __name__ == '__main__':
    main()
