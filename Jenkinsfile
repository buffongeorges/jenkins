pipeline{
    agent any
    
    stages{
        stage('build'){
           steps {
                withPythonEnv('python') {
                    bat 'pip install virtualenv'
                   
                    bat 'virtualenv venv --distribute'
              
                    bat 'python TEST.py'
                }
            }
        }
    }
}

