# PUC Specialization Thesis - Proof of concept

## Overview
The idea of this repository is to have a POC application running to present a Specialization Course Thesis.
The application consists of:
- Backend Microservice Cluster
- Frontend Client

### Backend Microservice Cluster
A collection of microservices that together deliver the objective of the application.
The microservices within the cluster are not accessible by direct API calls, all of the must be handled by the gateway which then, forwards the request for the suitable service.

The implementation in this repo presumes a full virtualized set of services, using Docker, that run on a Kubernetes cluster. Since it is just a POC, the simulation occurs using Docker-Copmose with a private network.

All the microservices respepct the boundaries of scope and are responsible for their matter, consulting others when it is necessary to retrieve out-ot-scope information and append to data.

#### Services Running
- Microservice-Disciplina - Controller of available subjects
- Microservice-Curso - Controller of available courses
- Microservice-Usuario - Controller of user management and auth generation
- Microservice-Gateway - Route manager for all services

### Frontend Client
Application using React with a series of components and Redux to manage the State. Besides the natural components, there are a series of components who are directly connected to the microservices, being the access interface to handle their data trough the available API.

#### Application Running
- Frontend - Web Application to access the Gateway methods

## Running
Running the application will make it possible to access public and private methods through the API and use the Frontend to navigate alongside data that is gathered from public endpoints.

### Requirements
You need to have the following applications installed in your environment.
- Docker [https://www.docker.com/]
- Docker Compose [https://docs.docker.com/compose/]
- Node [https://nodejs.org/]
- NPM [https://www.npmjs.com/]

### To Run
- Clone this repo
- Enter the folder

#### Backend
- Open the terminal, enter the folder and type `docker-compose up`
- Now the backend applications will be running.
- Keep the terminal open and running.

#### Frontend
- Open the terminal, enter the folder and then enter in *frontend* folder
- Type `npm install`to download all necessary packages to run the application
- Type `npm start`to start the application
- After complete go to the browser at `http://localhost:9000/` and check it running.

#### API Testing
In the repo there is a REST collection compatible generated by Insomnia REST Client that is compatible with Postman too.
