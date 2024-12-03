pipeline {
    agent any

    environment {
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
                $PIP install -r requirements.txt || true
                '''
            }
        }

        stage('Run App.py') {
            steps {
                // Run app.py to print "Hello, World!"
                sh '''
                $PYTHON app.py
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
                // Placeholder for deployment actions
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
