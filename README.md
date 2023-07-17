# Azure App Service QDrant Deployment

This repository provides an Azure Resource Manager (ARM) template for deploying [QDrant](https://github.com/qdrant/qdrant), a vector similarity search engine with extended filtering support, to Azure Web App for Containers. It also demonstrates how to leverage Azure's built-in authentication for secure access to QDrant.

## Prerequisites

Before proceeding with this guide, make sure you have:

- An active Azure account. If you don't have one, you can create a [free account](https://azure.microsoft.com/en-us/free/) before you begin.

## Deployment

Deploying the application to Azure is as simple as clicking the "Deploy to Azure" button below.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FSoftlandia-Ltd%2Fqdrant-azure-app-service%2Fmain%2Ftemplate.json)

The link will direct you to the Azure portal with pre-filled parameters from the ARM template. You'll need to fill in any remaining necessary parameters (e.g., subscription, resource group, app service names etc.), then click "Review + create" to validate and deploy the template.

## Post Deployment Configuration

After successful deployment, you need to enable Azure's built-in authentication:

1. Go to the Azure portal and navigate to your App Service.
2. Under the "Settings" menu, click on "Authentication".
3. Click "Add identity provider".
4. Use the following settings, replace "GetStartedWebApp" with your own app name:
![Authentication Settings](https://learn.microsoft.com/en-us/azure/app-service/media/scenario-secure-app-authentication-app-service/configure-authentication.png)
5. See the detailed guide below for a Python example that accesses the QDrant database

## Detailed Guide

Link coming soon
