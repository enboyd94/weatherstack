FROM python:3.10.12

#Make a directory within my Dockerfile
RUN mkdir my_code

#Set that working directory
WORKDIR /my_code

#Add the code to the working directory
COPY ./ /my_code/

#Install requirements
RUN pip install -r requirements.txt

#Open a bash shell
CMD ["/bin/bash"]