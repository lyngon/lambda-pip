#!/bin/bash

echo ${INPUT_DIR}
echo ${OUTPUT_DIR}

home=`pwd` &&
mkdir -p python &&
cd ${INPUT_DIR} &&
pip install -t ${home}/python/ $@ &&
cd ${home} &&
zip -r ${OUTPUT_DIR}/package.zip python
