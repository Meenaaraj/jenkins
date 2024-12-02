pipeline {
    agent any

    tools {
        git 'Default'  // Ensure the correct Git tool is used
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'Meena',  // Replace with your actual credentialsId
                    url: 'https://github.com/Meenaaraj/jenkins.git',
                    branch: 'main'
            }
        }

        stage('Set up Python') {
            steps {
                sh 'sudo apt-get update'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'sudo apt-get install -y python3 python3-pip'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 setup.py install'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying to production"'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
