Ansible Role: Molecule
======================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-molecule.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-molecule)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.molecule-blue.svg)](https://galaxy.ansible.com/gantsign/molecule)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-molecule/master/LICENSE)

Ansible role for installing the [Molecule](https://molecule.readthedocs.io) test tool for Ansible.

Requirements
------------

* Ansible

    * 2.0
    * 2.1

* Ubuntu

    * Wily (15.10)
    * Xenial (16.04)
    * Note: newer Ubuntu versions may work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The version of Molecule to install
molecule_version: '1.11.0'

# Directory to store files downloaded for Molecule installation
molecule_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - role: gantsign.molecule
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
