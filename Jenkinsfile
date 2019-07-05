pipeline{
    agent any
    
    stages{
        stage('build'){
           agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                withPythonEnv('python') {
                    bat 'virtualenv venv --distribute'
                    bat 'source venv/bin/activate '
                    bat 'pip install --user -r requirements.txt'
                    bat 'python WebChecker.py'
                }
            }
        }
    }
}

