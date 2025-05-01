pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git(
          url: 'https://github.com/khushii007/hello-docker-app.git',
          branch: 'main',                     // ← force main
          credentialsId: 'github-usrpwd'
        )
      }
    }
    stage('Build & Push') {
      steps {
        script {
          // Build
          docker.build("khushii007/hello-docker-app:${BUILD_NUMBER}")
          // Login
          withCredentials([usernamePassword(
            credentialsId: 'dockerhub-cred',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
          )]) {
            sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
          }
          // Push
          sh "docker push khushii007/hello-docker-app:${BUILD_NUMBER}"
        }
      }
    }
    stage('Run Container') {
      steps {
        sh 'docker run --rm khushii007/hello-docker-app:${BUILD_NUMBER}'
      }
    }
  }
}
