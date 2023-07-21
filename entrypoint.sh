
# entrypoint.sh

#!/bin/bash

#gunicorn -k uvicorn.workers.UvicornWorker --port $WEBSITES_PORT app:app
#gunicorn --port $PORT app:app
gunicorn app:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker 
#gunicorn -k uvicorn.workers.UvicornWorker --bind=0.0.0.0 --port $PORT --timeout 600 hello:app
