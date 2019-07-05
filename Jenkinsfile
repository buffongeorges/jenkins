pipeline{
    agent any
    
    stages{
        stage('build'){
            steps{  
                bat """pip install py"""
                
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
