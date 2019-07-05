pipeline{
    agent any
    
    stages{
        stage('build'){
            steps{
                withPythonEnv('python') {
                    bat """pip install py"""
                }
            }
        }
        
        stage('test'){
            steps{
                withPythonEnv('python') {
                    bat """
                    py TEST.py
                """
                }
            }
        }
    }
}
