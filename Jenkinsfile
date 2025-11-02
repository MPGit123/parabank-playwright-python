pipeline {
    agent any

    environment {
        // Path where Python installs venv (workspace folder)
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python & Install Dependencies') {
            steps {
                bat """
                python -m venv %VENV%
                call %VENV%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install playwright pytest pytest-playwright allure-pytest
                playwright install
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                call %VENV%\\Scripts\\activate
                pytest --junitxml=results.xml
                """
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'results.xml', fingerprint: true
            junit 'results.xml'
        }
    }
}
