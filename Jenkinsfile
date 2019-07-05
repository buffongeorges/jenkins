pipeline{
    agent any
    
    stages{
        stage('build'){
           steps {
                withPythonEnv('python') {
                    bat 'pip install virtualenv'
                   
                    bat 'virtualenv venv --distribute'
                
                    
                    bat 'pip install -r requirements.txt'
                    bat 'python TEST.py'
                }
            }
        }
    }
}

