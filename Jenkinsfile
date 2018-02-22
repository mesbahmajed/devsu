#!groovy

pipeline {
  agent any

 triggers {
        pollSCM '* * * * *'
    }
  stages {
    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */
        checkout scm
    }
    stage('App tests') {
    steps {
        sh 'py.test --junitxml results.xml run.py'
      }
    }
    stage('Docker Build') {
    steps {
        sh 'cd $WORKSPACE/app && docker build -t example_app:latest .'
      }
    }
    stage('Docker Push') {
      agent any
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push example_app:latest'
        }
      }
      
   }
}
