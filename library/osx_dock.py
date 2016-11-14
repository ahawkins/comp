#!/usr/bin/env python

from ansible.module_utils.basic import *

def osx_dock_absent(module, args):
    name = args['name']

    find_status, find_stdout, find_stderr = module.run_command([ 'dockutil', '--find', name ], check_rc=False)

    if find_status == 0:
        remove_status, remove_stdout, remove_stderr = module.run_command([ 'dockutil', '--remove', name ], check_rc=True)
        return False, True, remove_stdout
    else:
        return False, False, find_stdout

def osx_dock_present(module, args):
    name, path = args['name'], args['path']
    changed_status = False

    find_status, find_stdout, find_stderr = module.run_command([ 'dockutil', '--find', name ], check_rc=False)

    # Add to the dock if not present
    if find_status != 0:
        add_status, add_stdout, add_stderr = module.run_command([ 'dockutil', '--add', path ], check_rc=True)
        changed_status = True

    # Move dock item if position given
    if args.get('Position'):
        module.run_command([ 'dockutil', '--move', name, '--position', args['position'] ], check_rc=True)
        changed_status = True

    return False, changed_status, 'OK'
def main():
    fields = {
        "name": { "required": True, "type": "str" },
        "position": { "required": False, "type": "int" },
        "path": { "required": False, "type": "str" },
        "state": {
            "default": "present",
            "choices": [ 'absent', 'present' ],
            "type": 'str'
        },
    }
    choice_map = {
        "present": osx_dock_present,
        "absent": osx_dock_absent
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, stdout = choice_map.get(module.params['state'])(module, module.params)

    if is_error:
        module.fail_json(msg=stdout)
    else:
        module.exit_json(changed=has_changed, stdout=stdout)

if __name__ == '__main__':
    main()
