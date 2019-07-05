pipeline{
    agent any
    
    stages{
        stage('build'){
           steps {
                withPythonEnv('python') {
                    bat 'pip install virtualenv'
                    bat 'pip install source'
                    bat 'virtualenv venv --distribute'
                    bat 'source venv/bin/activate '
                    bat 'pip install --user -r requirements.txt'
                    bat 'python WebChecker.py'
                }
            }
        }
    }
}

