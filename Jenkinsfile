pipeline{
    agent any
    
    stages{
        stage('build'){
           steps {
                withPythonEnv('python') {
                    bat 'pip install virtualenv'
                   
                    bat 'virtualenv venv --distribute'
                     bat 'pip install source'
                    bat 'source venv/bin/activate '
                    bat 'pip install --user -r requirements.txt'
                    bat 'python WebChecker.py'
                }
            }
        }
    }
}

