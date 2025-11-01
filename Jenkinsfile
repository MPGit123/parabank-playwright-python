pipeline{
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:latest'
        }
    }

    environment {
        REPORT_DIR = "reports"
    }

    stages {
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }

        stage ('Install dependencies') {
            steps {
                sh 'mkdir -p ${REPORT_DIR}'

                script {
                    if (fileExists(requirements.txt)) {
                        sh 'pip install -r requirements.txt'
                    }
                    else {
                        sh 'pip install pytest pytest-playwright playwright'
                    }
                }

                sh 'playwright install --with-deps || playwright install'
            }
        }

        stage ('Run Test') {
            steps {
                sh '''
                    pytest --alluredir=${REPORT_DIR}/allure-results --junitxml=${REPORT_DIR}/results.xml
                    '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([results: [[path: "${REPORT_DIR}/allure-results"]], reportBuildPolicy: 'ALWAYS'])
            }
        }
    }
}