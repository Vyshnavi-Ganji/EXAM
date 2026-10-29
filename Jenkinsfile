pipeline{
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                bat 'docker build -t myappflaskapp .'
            }
        }
        stage('Run') {
            steps {
                echo 'Running the Docker container...'
                bat 'docker rm -f mycontainer || exit 0'
                bat 'docker run -d -p 5000:5000 --name mycontainer myappflaskapp'
            }
        }
    }
    post{
        success{
            echo 'Pipeline completed successfully.'
        }
        failure{
            echo 'Pipeline failed.'
        }
    }
}