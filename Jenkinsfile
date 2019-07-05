pipeline{
    agent any
    
    stages{
        stage('build'){
           steps {
                withPythonEnv('python') {
                    bat 'pip install virtualenv'
                   
                    bat 'virtualenv venv --distribute'
                
                    
                    bat 'pip install --user -r requirements.txt'
                    bat 'python TEST.py'
                }
            }
        }
    }
}

