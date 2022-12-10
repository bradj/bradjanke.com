---
title: "About"
# date: 2022-01-26T00:40:24-06:00
draft: false
tags: []
---

Hi. I'm Brad. I'm a Lead Engineer with over 13 years of experience and a passion for workflow automation. I enjoy replacing manual and repetitive tasks with maintainable solutions, delivering quality products to end users that make their lives measurably simpler, and solving problems with my peers. I have a notable mix of full stack and cloud/infra management experience which allows me to be productive across an entire stack.

# Experience

## CloudKnit - Founding Engineer
April 2022 - Current

**CloudKnit** is a SaaS offering that helps make cloud environment management easy.  I automated the entire SDLC process for faster deployment which took the deploy process from over 1 hour to ~5 minutes:

* Redesigned architecture to be multi-tenant
* Implemented design decisions across all layers of the system: backend web services, k8s operator, Argo CD, React web app, and database
* As part of the redesign, replaced a self-managed Dex IdP with hands-off Auth0
* Replaced time consuming deployments with Github Actions across all app repos 
* Automated Helm chart deployments
* Designed and implemented account self-registration

## MTN Development - Owner
February 2017 - Ongoing

I created MTN as a consulting umbrella. While working as a consultant I've been able to accomplish the following:

* Worked on open source Terraform modules and cloud transformation to AWS during a stint at [Cloud Posse](https://github.com/cloudposse/)
* Simultaneously managed relationships with several clients which involved outlining problem areas, creating resolution plans, and executing on my own or while guiding client engineers
* Projects largely revolved around AWS infrastructure management via Terraform
* Clients typically had no or little Terraform experience which allowed me to provide Terraform training while delivering solutions
* Focused on fragmented or non-existent CICD pipelines (mostly Jenkins and Github Actions) with the goal of automating as much as possible

## Optum - Lead Software Engineer
June 2020 - February 2021

* Designed and led the implementation of a new Event Driven PII Data Ingestion and Validation solution in Azure. This solution utilizes Data Factory to orchestrate Databricks and Azure Functions to run preliminary validation pipelines. Data Factory pipelines are generated from client configurations. Client configurations are managed by non-technical users so engineering time is spent on the platform.
* Implemented serverless validation pipeline using Azure Function Apps. Pipeline is triggered by Storage events. Monitored via Log Analytics and App Insights
* File level validation is performed across several batches where each batch can consist of 100s of GB of data
* Spark jobs handles row level validation so that we can more easily distribute load across the Azure Databricks cluster
* All Azure infrastructure is managed by Terraform
* Acted as Scrum Master, Project Manager, and Engineering Lead on a team of 5

## Fielda - Consultant
March 2020 - August 2020

I started with the goal of managing their application infra from Terraform on AWS. They had a mix of manual and automated steps but hadn't completely committed to an IaC direction. I was able to accomplish the following:

* Migrated applications away from bare EC2 instances into ECS Fargate
* Migrated CICD pipelines from Jenkins into Github Actions which pushed to ECR
* Configured CloudWatch alarms and Dashboards to show and alert on metrics that matter
* Using Terraform, they're now able to stand up a completely new environment running in a completely new AWS account in under 30 minutes. This process allows them to add ephemeral environments into their workflow, on infra that mirrors their production environment, while allowing the engineering work to continue uninterrupted on their regular development & staging environments.

## LiveSchool - Senior Backend Engineer
February 2019 - March 2020

While at LiveSchool my goal was to improve our engineering workflows. I focused on automation and operational efficiency of the CI/CD stack and its supporting services.\n\n Built infrastructure for managing build pipelines. Implemented Config and Secret management; killed our self hosted Jenkins cluster by moving to Github Actions for builds and versioned artifacts.\n\n Developed tooling to automate infrastructure operations. Created a Platform with VPN that’s home to our engineering tools and an Admin Panel to manage environments; infra managed with Terraform; reduced  cost and maintenance by transitioning to Serverless architecture.

* Reduced end of year School Rollovers from >60 minute execution times to <10 minutes by porting PHP into serverless Node and optimizing the database to better support the Rollover queries. Implemented a UI for Rollovers that gives immediate feedback  on the status of past and currently processing Rollover operations.
* Implemented config management using confd and AWS SSM. Containers now hydrate configs on startup. Managed IAM Roles and Policies via Terraform to control Parameter Store access.
* Switching environments at LiveSchool was time consuming so I researched what features engineering used most, ported those into the Admin Panel that lives within the engineering Platform, and provided access across all environments so that engineers can quickly pivot across environments.

## Contino - Senior DevOps Consultant
October 2018 - February 2019

* Worked onsite within a team of four in Dallas, TX to help guide an organization into AWS. We worked with engineers and directors to discover shortcomings and implement both cultural and technical changes to ease the transition into AWS.
* Created a generic Jenkins build process that gave AppDev teams a path to follow while migrating their applications and builds. This process handled static code analysis, unit & integration tests, tagging & versioning, and pushing artifacts to private registries.
* Demonstrated how one could integrate Docker into everyday workflows by having your application containerized. These demonstrations paired well  with showing off the new Jenkins pipeline by simultaneously demonstrating automatic builds & tests mixed with ready to deploy artifacts.

## Rackspace - Platform Engineer
October 2016 - September 2018

* Operated within the Developer Services team in a 100% remote organization. I worked on a team of around 35 engineers while acting as product owner of the CLI and SDK’s for the Trebuchet Platform as a Service on Kubernetes. My focus was entirely on simplifying developer workflows through automation.
* Helped create “one-click” deployment CLI (Splat) which provided an entry point into app orchestration by allowing users to generate custom application footprints by choosing their tech stack. Splat supported several stacks such as Python, JS, GO, and Ruby as well as in-memory, nosql,  and/or relational databases.
* The CLI for the Trebuchet Platform was automatically generated from Swagger specs. This automation allowed me to quickly update the CLI based on upstream service changes. Each service that wanted to be consumed via the CLI could add a snippet in their build process that would trigger the CLI to be rebuilt and consume any changes done to the service interface.

## Change Healthcare - Senior Software Engineer
April 2016 - August 2016

* Focused on front end development with React
* Development lead for new features. I was in charge of redesigning old components to new emitter patterns. The application followed the Flux pattern which employs a catch all mentality. We decided an explicit event based approach is a better fit for our purposes. I was lead on new development with this pattern

## Kanini - Senior Software Engineer
October 2014 - April 2016

* Designed and implemented application infrastructure using AWS. The infrastructure would automatically handle scaling, backups of logs and data, and daily reports
* Created multi-tenant API in Node.js. This API is in charge of handling every transaction from mobile and  web apps. It sits on top of Postgres, Redis, and RabbitMQ

## GISi - Senior Software Engineer (Contract)
April 2014 - September 2014

* Built solutions with ESRI’s ArcGIS Desktop and JavaScript libraries

## Titan Cloud - Senior Software Engineer
April 2013 - April 2014

## Kanini - Software Engineer
April 2010 - April 2013

* Created several GIS solutions using ESRI & Mapbox

## PlantCML/Dialogic Communications
September 2007 - February 2010

* Designed and implemented high throughput SMS gateway to simultaneously process millions of messages
