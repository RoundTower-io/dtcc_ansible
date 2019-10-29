pipeline {
    agent "spvlanautomation01.lab.dtcc.com"
    parameters {
        string(name: 'VLAN', defaultValue: '', description: '')
    }
    stages {
        stage("Git Clone") {
            steps {
                sh 'https_proxy="https://172.26.136.21:80" git clone https://github.com/RoundTower-io/dtcc_ansible.git'
            }
        }
        stage("Find VLAN File") {
                echo "VLAN is ${params.VLAN}"
                sh 'pwd; ls '
        }
    }
}