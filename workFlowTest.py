name: Deploy to Cloud Run

on:
  push:
    branches:
      - main  # Change if your default branch is 'master'
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      for i in range(5):
        print("Anurag1")
        sleep(5)
        print("Anurag2")
