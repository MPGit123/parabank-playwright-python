pipeline {
    agent any

    parameters {
        choice (name: 'TEST_SUIT', choices: ['smoke', 'regression', 'all'], description: 'Which test to run?')
    }

    environment {
        // Path where Python installs venv (workspace folder)
        VENV = "venv"
        PLAYWRIGHT_BROWSERS_PATH = "C:\\Users\\Mayank.Patel\\.jenkins\\playwright_browsers"
        PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD = "1"
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
                playwright install chromium
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                call %VENV%\\Scripts\\activate
                if "%TEST_SUIT%"=="smoke" (pytest -m smoke --junitxml=results.xml) ^
                else if "%TEST_SUIT%"=="regression" (pytest -m regression --junitxml=results.xml) ^
                else (pytest --junitxml=results.xml)
                """
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
