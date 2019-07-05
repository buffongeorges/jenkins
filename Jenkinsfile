pipeline{
    agent any
    
    stages{
        
        stage('test'){
            steps{
                bat """
                
                    pip install py
                    py TEST.py
                """
                
            }
        }
    }
}
