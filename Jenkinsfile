pipeline {
    agent any

    stages {
        stage('Setup Virtual Environment') {
            steps {
                bat '''
                echo Setting up the virtual environment
                
                REM Remove existing virtual environment if it exists
                if exist mlip rmdir /S /Q mlip

                REM Create a new virtual environment
                python -m venv mlip

                REM Activate the virtual environment
                call mlip\\Scripts\\activate.bat

                REM Upgrade pip (optional but recommended)
                python -m pip install --upgrade pip

                REM Install required packages
                pip install pytest numpy pandas scikit-learn

                REM Deactivate the virtual environment
                call mlip\\Scripts\\deactivate.bat
                '''
            }
        }
        stage('Build') {
            steps {
                bat '''
                echo Build step: Skipped for Python projects
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

                REM Deactivate the virtual environment
                call mlip\\Scripts\\deactivate.bat
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
