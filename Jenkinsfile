pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = 'python3'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub repository
                git 'https://github.com/Meenaaraj/jenkins.git'
            }
        }

        stage('Set up Python') {
            steps {
                // Install Python 3
                sh '''
                    sudo apt-get update
                    sudo apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install any dependencies listed in requirements.txt (if applicable)
                // sh 'pip3 install -r requirements.txt'  // Uncomment if you have dependencies
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using unittest
                sh 'python3 -m unittest discover -s . -p "test_*.py"'
            }
        }

        stage('Build') {
            steps {
                // For demonstration, just echo a message as the build step
                echo 'Build completed successfully.'
            }
        }

        stage('Deploy') {
            steps {
                // Placeholder for deploy steps (you can integrate your deployment here)
                echo 'Deploying application...'
            }
        }
    }

    post {
        success {
            echo 'Build and test completed successfully!'
        }
        failure {
            echo 'Build or test failed.'
        }
    }
}
