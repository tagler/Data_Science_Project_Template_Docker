FROM continuumio/miniconda3:4.8.2

RUN conda install --quiet --yes \
    'numpy=1.18.1' \
    'pandas=1.0.3' \
    'scikit-learn=0.22.1' \
    'networkx=2.4' \
    'matplotlib=3.1.3' \
    'seaborn=0.10.0' \
    'black=19.10b0' \
    'jupyterlab=1.2.6'
    
RUN mkdir /project_working_directory

WORKDIR /project_working_directory

EXPOSE 8888

#CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]
