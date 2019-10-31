node("Ansible") {
    parameters {
        string(name: 'VLAN', defaultValue: '', description: '')
    }
    stage("PreClean") {
        echo "Looking for old directories"
        sh 'pwd; ls'
        sh 'if [ -d "dtcc_ansible" ]; then rm -rf "dtcc_ansible"; fi'
    }
    stage("Git Clone") {
       sh 'https_proxy="https://172.26.136.21:80" git clone --recurse-submodules https://github.com/RoundTower-io/dtcc_ansible.git'
    }
    stage("Run Ansible") {
        echo "VLAN is ${params.VLAN}"
        if (fileExists("dtcc_ansible/test_vlans/dtcc/vlan_${params.VLAN}.yml")) {
            sh "cd dtcc_ansible; /usr/local/bin/ansible-playbook -i ./dtcc_hosts ./snapshot_host_config.yml --extra-vars=\'@test_vlans/dtcc/vlan_${params.VLAN}.yml\'"
            sh "cd dtcc_ansible; /usr/local/bin/ansible-playbook -i ./dtcc_hosts ./create_vlan.yml --extra-vars=\'@test_vlans/dtcc/vlan_${params.VLAN}.yml\'"
            sh "cd dtcc_ansible; /usr/local/bin/ansible-playbook -i ./dtcc_hosts ./snapshot_host_config.yml --extra-vars=\'@test_vlans/dtcc/vlan_${params.VLAN}.yml\'"
        } else {
            error("Cannot find any configuration file for VLAN ${params.VLAN}")
        }
    }
}

