pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = 'python3'
    }

    stages {
          stage('Checkout'){
           steps {
                git credentialsId: 'Meena',
                url: 'https://github.com/Meenaaraj/jenkins',
                branch: 'main'

            }
        }

        stage('Set up Python') {
            steps {
                // Install Python 3 and pip, along with python3-venv for virtualenv support
                sh '''
                    sudo apt-get update
                    sudo apt-get install -y python3 python3-pip python3-venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'This is a valid stage with steps.'
                // If you have a requirements.txt, install dependencies
                // sh 'pip3 install -r requirements.txt'  // Uncomment this if you have a requirements.txt
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
