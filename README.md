# Image and Text Generation with Amazon Titan, Llama, and FAISS


This project demonstrates the use of Amazon Titan for image generation, Titan Embedding for text generation, Llama for text generation, LangChain for managing AI workflows, FAISS for vector storage, and boto3 for AWS interaction. The goal of the project is to showcase the integration of multiple state-of-the-art models and tools to generate high-quality text and images, store embeddings in a vector database, and efficiently manage AI workflows.

## Table of Content
- Overview
- Prerequisites
- Installation 
- Usage


## Overview

This project combines state-of-the-art AI models to generate images and text based on various prompts:

- Amazon Titan: A powerful image generation model used to generate images from textual descriptions.
- LLaMA: A text generation model capable of creating high-quality text outputs based on input prompts.
- Titan Embedding: Used to convert text into vector embeddings that capture semantic meaning.
- LangChain: A framework for orchestrating AI workflows, used here to manage the generation of text and images, as well as the processing of embeddings and interactions between models.
- FAISS: A vector database that stores and retrieves embeddings efficiently, allowing for quick nearest neighbor searches.
- boto3: Utilized for interacting with AWS services like Amazon S3 for data storage and managing resources.

## Prerequisites
- boto3
- awscli
- pypdf
- langchain
- streamlit
- faiss-cpu

## Installation

1. Install Dependencies 
```bash
pip install -r requirements.txt
```

2. Set up AWS credentials: If you haven't already, configure AWS CLI with your credentials:
```bash
aws configure
```
3. Install FAISS: FAISS may need to be installed separately depending on your system. Follow the installation instructions from the `FAISS GitHub page`.

## Conclusion 
This project integrates Amazon Titan, LLaMA, Titan Embeddings, LangChain, FAISS, and boto3 to create a full pipeline for generating images and text, storing embeddings, and managing AI workflows. By combining these powerful tools, the project demonstrates how AI models and vector databases can be used together for a wide range of tasks.
