pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        PIP = 'pip3'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git(
                    url: 'https://github.com/Meenaaraj/jenkins.git',
                    branch: 'main',  // specify the branch explicitly
                    credentialsId: 'github-credentials'
                )
            
        }
    }
        }

        stage('Set Up Python Environment') {
            steps {
                sh '''
                $PIP install --upgrade pip
                $PIP install -r requirements.txt || true
                '''
            }
        }

        stage('Check Workspace') {
            steps {
                // List files in the workspace to confirm app.py is present
                sh 'ls -al'
            }
        }

        stage('Run App.py') {
            steps {
                echo 'Running app.py'
                sh '''
                $PYTHON app.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                $PYTHON -m pytest test_app.py --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying app...'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up after build'
        }

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
