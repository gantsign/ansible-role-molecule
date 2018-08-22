import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_molecule(host):

    # Check the `molecule` executes successfully.
    assert host.run('molecule --version').rc == 0
