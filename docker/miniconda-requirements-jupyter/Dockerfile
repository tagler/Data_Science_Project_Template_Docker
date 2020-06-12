FROM continuumio/miniconda3:4.8.2

#COPY environment.yml /tmp/environment.yml
COPY requirements.txt /tmp/requirements.txt

#RUN conda env update --name base --file /tmp/environment.yml
RUN conda env update --name base --file /tmp/requirements.txt

RUN mkdir /project_working_directory

WORKDIR /project_working_directory

EXPOSE 8888

#CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]
