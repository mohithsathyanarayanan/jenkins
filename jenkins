pipeline { 
agent any
    stages {
        stage('Get repositery') {
            steps {
                git 'https://github.com/mohithsathyanarayanan/jenkins.git'
            }
        }
        stage('Source code') {
            steps {
                sh "/usr/bin/python3 add.py"
            }
        }
        stage('Testing phase') {
            steps {
                sh "/usr/bin/python3 test.py"
            }
        }
    }
}    
