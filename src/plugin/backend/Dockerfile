FROM python:3.9-slim

# Maintainer info
LABEL maintainer="khaledihkh@gmail.com"

# Make working directories
RUN  mkdir -p  /fastapi_flair
WORKDIR  /fastapi_flair

# Upgrade pip with no cache
RUN pip install --no-cache-dir -U pip

# Copy application requirements file to the created working directory
COPY requirements.txt .

# Install application dependencies from the requirements file
RUN pip install -r requirements.txt

# Copy every file in the source folder to the created working directory
COPY  fastapi_flair .

# Run the python application
CMD ["api.main:app"]