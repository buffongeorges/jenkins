pipeline{
    agent any
    
    stages{
        
        stage('test'){
            steps{
                script {
                    withPythonEnv('python'){
                        bat "python TEST.py"
                    
                    }
                
                }
        }
    }
}
    
}
