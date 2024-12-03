pipeline {
    agent any

    environment {
        // Define environment variables if needed
        PYTHON = 'python3'
        PIP = 'pip3'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone your repository containing the Python files
                git 'https://github.com/Meenaaraj/jenkins.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                // Install dependencies (if you have requirements.txt)
                sh '''
                $PIP install --upgrade pip
                $PIP install -r requirements.txt || true  # if you have requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh '''
                $PYTHON -m pytest test_app.py --maxfail=1 --disable-warnings -q 
                '''
            }
        }

        stage('Deploy') {
            steps {
                // Here you can deploy your application if needed
                echo 'Deploying app...'
            }
        }
    }

    post {
        always {
            // Clean up or post build actions
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

