# WEEK 1 PROJECT:  

## Simple microservice application  

 1. Create a simple microservice application 

 2. Your application should contain two microservices: a frontend service and a backend service (with or without a database) 

 3. You can use any programming language of choice 

 4. Your frontend service should fetch the word “TALENT PLUS” from the backend service using an API call. 

## SOLUTION 
A Simple AWS Beanstalk App (http://talent-env.eba-dpqkmvpu.us-west-2.elasticbeanstalk.com/) backed by a combined serverless backend (following an event driven microservice paradigm): AWS lambda, AWS API Gateway and
AWS DynamoDB

The lambda function calls the get-item api of aws dynamodb to get the "TALENT PLUS" word from this managed NoSQL Database, and the api gateway resource wraps the lambda function into a rest api. Finally, a simple flask microservice that supports front end calls the api-gateway api url to retrieve the result for display, this flask microservice is dockerized and hosted on AWS Elastic Beanstalk, a PaaS.

Programming language used: PYTHON