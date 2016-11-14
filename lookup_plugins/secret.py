from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
import keyring

class LookupModule(LookupBase):
    def run(self, terms, variables, **kwargs):
        ret = [ ]

        for term in terms:
            result = keyring.get_password(term, None)

            if result:
                ret.append(result)
            else:
                raise AnsibleError('Lookup {} Failed'.format(term))

        return ret
