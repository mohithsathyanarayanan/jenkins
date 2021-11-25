
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
                sh "/usr/bin/python3 /home/mohith/Downloads/add.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "/usr/bin/python3 /home/mohith/Downloads/test.py"
            }
        }
    }
}    
