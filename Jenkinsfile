pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git(
          url: 'https://github.com/khushiii007/hello-docker-app.git',
          credentialsId: 'github-token'
        )
      }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t hello-docker-app:${BUILD_NUMBER} .'
      }
    }
    stage('Run Container') {
      steps {
        // Demonstrate it works
        sh 'docker run --rm hello-docker-app:${BUILD_NUMBER}'
      }
    }
  }
}
