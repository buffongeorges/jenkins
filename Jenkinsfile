pipeline{
    agent any
    
    stages{
        stage('build'){
            steps{  
                pip install py
                
            }
        }
        
        stage('test'){
            steps{
                bat """
                    py TEST.py
                """
                
            }
        }
    }
}
