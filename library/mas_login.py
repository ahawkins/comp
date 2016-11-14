#!/usr/bin/env python

from ansible.module_utils.basic import *

def mas_login_present(module, args):
    email, password = args['email'], args['password']

    account_status, account_stdout, account_stderr = module.run_command([ 'mas', 'account' ], check_rc=True)

    if account_stdout.find(email) == -1:
        login_status, login_output, login_stderr = module.run_command([ 'mas', 'login', email, password ], check_rc=True)
        return False, True, login_output
    else:
        return False, False, account_stdout

def main():
    fields = {
        "email": { "required": True, "type": "str" },
        "password": { "required": True, "type": "str" },
        "state": {
            "default": "present",
            "choices": [ 'present' ],
            "type": 'str'
        },
    }
    choice_map = {
        "present": mas_login_present
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, stdout = choice_map.get(module.params['state'])(module, module.params)

    if is_error:
        module.fail_json(msg=stdout)
    else:
        module.exit_json(changed=has_changed, stdout=stdout)

if __name__ == '__main__':
    main()
