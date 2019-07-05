pipeline{
    agent any
    
    stages{
        stage('build'){
            steps{
                PYENV_HOME=$WORKSPACE/.sample1/ 
virtualenv —no–site–packages $PYENV_HOME
. $PYENV_HOME/bin/activate 
nosetests —with–xunit tests
                
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
