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

### Frontend Client
Application using react with a series of components. Besides the natural components, there are a series of components who are directly connected to the microservices, being the access interface to handle their data trough the available API.
