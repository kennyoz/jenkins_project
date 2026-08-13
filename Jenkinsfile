pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Docker') {
            steps {
                sh 'docker --version'
                sh 'docker-credential-desktop version'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t fastapi-project .'
            }
        }
    }
}