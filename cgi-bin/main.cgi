#!/bin/bash
echo -en "Content-Type: text/plain\r\n\r\n"
ls -a ..${REQUEST_URI#${SCRIPT_NAME}}
