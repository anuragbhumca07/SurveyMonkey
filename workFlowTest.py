name: Deploy to Cloud Run

on:
  push:
    branches:
      - main  # Change if your default branch is 'master'
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      print("Anurag1")
      sleep(60)
      print("Anurag2")
