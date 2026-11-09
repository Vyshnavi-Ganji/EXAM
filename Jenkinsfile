pipeline{
    agent any
    stages{
        stage("BUILD"){
            steps{
                echo "Building Docker image..."
                bat 'docker build -t mypythonflaskapp .'
            }
        }
        stage("RUN"){
            steps{
                echo "Running Docker container..."
                bat 'docker rm -f mycontainer || exit 0'
                bat 'docker run -d -p 5000:5000 --name mycontainer mypythonflaskapp'
            }
        }
    }
    post{
        success{
            echo "Pipeline completed successfully."
        }
        failure{
            echo "Pipeline failed."
        }
    }
}