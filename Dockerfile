FROM ubuntu:xenial

RUN \
  apt-get update --yes && \
  apt-get install -y wget bzip2 build-essential cmake libffi-dev libatlas-base-dev liblapack-dev liblapacke-dev
RUN \
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
  bash Miniconda3-latest-Linux-x86_64.sh -b
RUN \
  /root/miniconda3/bin/conda config --set always_yes yes --set changeps1 no && \
  /root/miniconda3/bin/conda create -n testenv python=${PYTHONVERSION}

COPY . /app

# RUN \
#   /bin/bash -c "source /root/miniconda3/bin/activate testenv && which python && python -V && pip install nose coveralls && cd app && ls && python setup.py install && nosetests --with-coverage --cover-package=prox_tv"
RUN \
  cd app && \
  mkdir -p build && cd build && cmake -DENABLE_TESTING:BOOL=ON ../ && cmake --build . && ctest -VV


