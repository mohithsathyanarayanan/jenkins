
pipeline { 
agent any
    stages {
        stage('Clone Git Repository') {
            steps {
                git 'https://github.com/mohithsathyanarayanan/jenkins.git'
            }
        }
        stage('Run Code') {
            steps {
                sh "/usr/bin/python3 add.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "/usr/bin/python3 test.py"
            }
        }
    }
}    
