pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    
    }

    stages {
        // Clone the GitHub repository
        stage('Clone Repository') {
            steps {
                git(
                    url: 'https://github.com/Meenaaraj/jenkins.git',
                    branch: 'main',  // Specify the branch explicitly
                    credentialsId: 'github-credentials'  // Make sure this credentials ID is correct
                )
            }
        }

        // Set up Python environment and install dependencies
        stage('Set Up Python Environment') {
            steps {
                sh '''
                echo "Checking Python version"
                python3 --version

                echo "Checking pip version"
                which pip3 || echo "pip3 not found"
                pip3 --version || echo "pip3 not found"
                
                # If pip3 is not found, we will attempt to install it
                if ! command -v pip3 &> /dev/null; then
                    echo "pip3 not found, installing..."
                    python3 -m ensurepip --upgrade
                fi

                echo "Upgrading pip"
                python3 -m pip install --upgrade pip

                echo "Installing requirements"
                pip3 install -r requirements.txt || true
                '''
            }
        }

        // Check the workspace to ensure the required files exist
        stage('Check Workspace') {
            steps {
                echo 'Listing files in workspace to verify app.py and requirements.txt presence:'
                sh 'ls -al'
            }
        }

        // Run the Python app
        stage('Run App.py') {
            steps {
                echo 'Running app.py'
                sh '''
                python3 app.py
                '''
            }
        }

        // Run the tests using pytest
        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest'
                sh '''
                python3 -m pytest test_app.py --maxfail=1 --disable-warnings -q
                '''
            }
        }

        // Deploy stage (Add actual deployment steps here)
        stage('Deploy') {
            steps {
                echo 'Deploying app...'
                // Add your deployment steps here
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
