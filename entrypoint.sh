
# entrypoint.sh

#!/bin/bash

#gunicorn -k uvicorn.workers.UvicornWorker --port $WEBSITES_PORT app:app
gunicorn --port $WEBSITES_PORT app:app
