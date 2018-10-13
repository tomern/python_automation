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
                sh 'python /tests_folder/test_other.py'
            }
        }
    }
}