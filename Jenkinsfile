pipeline {
    agent none
    stages {
        stage('Tests') {
            agent {
                dockerfile {
                    dir 'tests_folder'
                    filename 'Dockerfile'
                }
            }
            steps {
                dir('tests_folder'){
                    sh 'pytest test_other.py --junit-xml=reports/report.xml'
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