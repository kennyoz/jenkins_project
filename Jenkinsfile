pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                sh '/usr/local/bin/docker build -t fastapi-project .'
            }
        }
    }
}