
import logging
import os
from . import utils
from policy import load_host_keys, get_policy_class, check_policy_setting

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_policy_setting(options, host_keys_settings):
    policy_class = get_policy_class(options.policy)
    logging.info(policy_class.__name__)
    check_policy_setting(policy_class, host_keys_settings)
    return policy_class()


def get_host_keys_settings(options):
    if not options.hostfile:
        host_keys_filename = os.path.join(base_dir, 'known_hosts')
    else:
        host_keys_filename = options.hostfile
    host_keys = load_host_keys(host_keys_filename)

    if not options.syshostfile:
        filename = os.path.expanduser('~/.ssh/known_hosts')
    else:
        filename = options.syshostfile
    system_host_keys = load_host_keys(filename)

    settings = dict(
        host_keys=host_keys,
        system_host_keys=system_host_keys,
        host_keys_filename=host_keys_filename
    )
    return settings


def check_encoding_setting(encoding):
    if encoding and not utils.is_valid_encoding(encoding):
        raise ValueError('Unknown character encoding {!r}.'.format(encoding))