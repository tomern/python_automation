pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'frolvlad/alpine-python3:latest'
                }
            }
            steps {
                sh 'python test_other.py'
            }
        }
    }
}