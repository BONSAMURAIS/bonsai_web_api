FROM continuumio/miniconda3 as basedeps

LABEL Description="This image holds a flask app for bonsai" Version="0.1.0"

#------------------------------------------------------------------------------
# Multi Stage Build: Download packages in this stage, and build later
#------------------------------------------------------------------------------
RUN conda install --download-only -c defaults conda  && conda update -n base -c defaults conda && conda install --download-only -c defaults -c conda-forge flask flask-security gunicorn

#------------------------------------------------------------------------------
# Install the deps from previous stage
#------------------------------------------------------------------------------
FROM continuumio/miniconda3 

COPY --from=basedeps /opt/conda/pkgs/ /opt/conda/pkgs
RUN conda update -n base -c defaults conda

RUN conda install -c conda-forge flask flask-security gunicorn

COPY . /app
WORKDIR /app
#RUN pip install -e .

RUN env FLASK_APP=bonsai_web_api flask init-db
ENTRYPOINT gunicorn -b :5000 bonsai_web_api:"create_app()"
