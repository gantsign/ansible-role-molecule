import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_molecule(Command):

    # Check the `molecule` executes successfully.
    assert Command('molecule --version').rc == 0
