pipeline{
    agent any
    
    stages{
        stage('build'){
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

