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
         sh "docker tag khushii007/hello-docker-app:${BUILD_NUMBER} khushii007/hello-docker-app:latest"
         sh "docker push khushii007/hello-docker-app:latest"
        }
      }
    }
    stage('Run Container') {
      steps {
        script {
          // 1. Start container in background
          def cid = sh(
            returnStdout: true,
            script: "docker run -d khushii007/hello-docker-app:${BUILD_NUMBER}"
          ).trim()
      
          // 2. Give it a moment to spin up
          sh 'sleep 5'
      
          // 3. Test the HTTP endpoint
          sh 'curl --fail http://localhost:8080 || (echo "Health check failed" && exit 1)'
      
          // 4. Cleanup
          sh "docker rm -f ${cid}"
        }
      }
    }

  }
}
