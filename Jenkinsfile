pipeline{
    agent any
    
    stages{
        
        stage('test'){
            steps{
                bat """
                
                    virtualenv -p /usr/bin/python3.7.3
                    py TEST.py
                """
                
            }
        }
    }
}
