pipeline {
    agent none
    stages {
        stage('Tests') {
            agent {
                dockerfile {
                    dir 'tests_folder'
                    filename 'Dockerfile'
                    args '--link mongo'
                    args '--network docker_default'
                }
            }
            steps {
                dir('tests_folder'){
                    sh 'pytest test_other.py -vv -n 2 -v --junit-xml=reports/report.xml'
                }
            }
            post {
                always {
                    junit 'tests_folder/reports/report.xml'
                }
            }
        }
    }
}