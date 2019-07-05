pipeline{
    agent any
    
    stages{
        stage('build'){
            steps{
                withPythonEnv('python') {
                    bat """pip install python
                    pip install python
                    py TEST.py"""
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
