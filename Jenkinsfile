pipeline {
    agent { label 'python3' }
    stages {
        stage("tests py") {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pytest -v --junitxml=report.xml tests.py'
            }
        }
    }
    post {
        always {
            archive '*.xml'
            junit allowEmptyResults: true, testResults: 'report.xml'
        }
    }
}
