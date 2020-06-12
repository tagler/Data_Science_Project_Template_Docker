FROM continuumio/anaconda3:2020.02

RUN conda install --quiet --yes \
    'black=19.10b0'

RUN mkdir /project_working_directory

WORKDIR /project_working_directory

EXPOSE 8888

#CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]
