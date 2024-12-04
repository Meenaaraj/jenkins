pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        PIP = 'pip3'
    }

    stages {
        // Stage to clone the repository
        stage('Clone Repository') {
            steps {
                git(
                    url: 'https://github.com/Meenaaraj/jenkins.git',
                    branch: 'main',  // Specify the branch explicitly
                    credentialsId: 'github-credentials'  // Make sure the credentialsId is correct
                )
            }
        }

        // Stage to set up Python environment
        stage('Set Up Python Environment') {
            steps {
                sh '''
                # Check Python version
                $PYTHON --version
                # Upgrade pip to latest version
                $PIP install --upgrade pip
                # Install dependencies (ignore errors if any)
                $PIP install -r requirements.txt || true
                '''
            }
        }

        // Stage to check the workspace and list files
        stage('Check Workspace') {
            steps {
                echo 'Listing files in workspace to verify app.py presence:'
                sh 'ls -al'
            }
        }

        // Stage to run the app.py script
        stage('Run App.py') {
            steps {
                echo 'Running app.py'
                sh '''
                # Run the app.py script
                $PYTHON app.py
                '''
            }
        }

        // Stage to run tests
        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest'
                sh '''
                # Run tests using pytest
                $PYTHON -m pytest test_app.py --maxfail=1 --disable-warnings -q
                '''
            }
        }

        // Stage to deploy the app (add deployment steps here)
        stage('Deploy') {
            steps {
                echo 'Deploying app...'
                // Add your deploy commands here
            }
        }
    }

    // Post actions to handle build results
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
