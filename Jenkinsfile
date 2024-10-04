pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''
                echo In C or Java, we can compile our program in this step
                echo In Python, we can build our package here or skip this step
                '''
            }
        }
        stage('Test') {
            steps {
                bat '''
                echo Test Step: We run testing tool like pytest here

                REM Activate the virtual environment
                call mlip\\Scripts\\activate.bat

                REM Run pytest
                pytest

                REM Comment out the exit 1 line after implementing Jenkinsfile
                REM exit 1
                '''
            }
        }
        stage('Deploy') {
            steps {
                bat '''
                echo In this step, we deploy our project
                echo Depending on the context, we may publish the project artifact or upload pickle files
                '''
            }
        }
    }
}
