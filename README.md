# dtcc_ansible
Ansible repo for the DTCC NetOps project

# What are these files and directories?

## plugins/filter
This is a collection of filter plugins. They are used to provide additional parsing and data manipulation not supplied 
by native Ansible.  Each filter has a brief description inside it.
 
## roles/parse_genie
This is the role which parses the NXOS output and puts data into a usable format. It comes from a separate repository and 
will be included when this repository is cloned. See .gitmodules below.

## test_vlans/dtcc
This contains the definitions for vlans.  Each vlan has one definition file.  The format of those files is discussed 
below. 

## .gitignore
This is a file instructing Git to ignore certain files

## .gitmodules
This file defines what other external repositories are to be included with this one when cloning.  That is, if you clone
this repository, the path in the .gitmodules file is included with it.  These are called submodules.

## ansible.cfg
The main config file for Ansible.  This tells Ansible where things like roles and plugins live.  It also contains the
path of the vault password file.

## create_vlan.yml
This creates vlans using input files found in `test_vlans/dtcc`

## delete_vlan.yml
This deletes a vlan using the same input files as `create_vlan.yml`

## dtcc_hosts
This file contains all the lab hosts Ansible knows about and how to reach them.  It also contains encrypted passwords.

## pipeline.groovy
This the pipeline definition for the Jenkins pipeline for `create_vlan.yml`

## README.md
This file.

## snapshot_host_config.yml
A small Ansible file to get a snapshot of the current running config of a Cisco switch




