from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_molecule(Command):
    # Cleanup any previous run.
    Command('rm -rf ansible-role-apt')

    # Checkout a simple Molecule project.
    assert Command('git clone --depth=1 --branch 1.1.3 %s',
                   'https://github.com/gantsign/ansible-role-apt.git').rc == 0

    # Check the `molecule test` completes successfully.
    assert Command('cd ansible-role-apt && molecule test').rc == 0
