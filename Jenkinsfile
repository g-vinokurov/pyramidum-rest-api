pipeline {
    agent any

    environment {
        REGISTRY = "docker.io"
        IMAGE_NAME = "kberk/rest_api_docs_app"
        DOCKER_CREDENTIALS_ID = "kberk"
        SSH_CREDENTIALS_ID = "3b7b9402-b9c7-4b99-aab3-8b7c48768e4e"
        SERVER_IP = "45.153.68.216"
        CONTAINER_NAME = "rest_api_docs_app"
        APP_PORT = "8000"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/pyramidum-space/rest-api-docs.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $REGISTRY/$IMAGE_NAME:$BUILD_NUMBER .'
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    }
                    sh 'docker push $REGISTRY/$IMAGE_NAME:$BUILD_NUMBER'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: env.SSH_CREDENTIALS_ID, keyFileVariable: 'SSH_KEY')]) {
                        sh """
                        ssh -i $SSH_KEY user@$SERVER_IP '
                        docker pull $REGISTRY/$IMAGE_NAME:$BUILD_NUMBER &&
                        docker stop $CONTAINER_NAME || true &&
                        docker rm $CONTAINER_NAME || true &&
                        docker run -d --name $CONTAINER_NAME -p 80:$APP_PORT $REGISTRY/$IMAGE_NAME:$BUILD_NUMBER
                        '
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

