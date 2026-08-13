pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:${env.PATH}"
        CONTAINER_NAME = "fastapi-test-container"
    }

    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t fastapi-project .'
            }
        }

        stage('Run application') {
            steps {
                sh 'docker run -d --name ${CONTAINER_NAME} -p 8000:8000 fastapi-project'
            }
        }

        stage('Wait for application') {
            steps {
                sh 'sleep 3'
            }
        }

        stage('Checkout tests') {
            steps {
                dir('tests') {
                    git branch: 'main',
                        url: 'https://github.com/kennyoz/jenkins_project_tests.git'
                }
            }
        }

        stage('Install test dependencies') {
            steps {
                dir('tests') {
                    sh 'python3 -m venv .venv'
                    sh '.venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run tests') {
            steps {
                dir('tests') {
                    sh '.venv/bin/pytest'
                }
            }
        }
    }

    post {
        always {
            sh 'docker stop ${CONTAINER_NAME} || true'
            sh 'docker rm ${CONTAINER_NAME} || true'
        }
    }
}