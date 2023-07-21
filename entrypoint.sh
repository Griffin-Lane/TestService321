
# entrypoint.sh

#!/bin/bash

#gunicorn -k uvicorn.workers.UvicornWorker --port $WEBSITES_PORT app:app
#gunicorn --port $PORT app:app

gunicorn --bind=0.0.0.0 --port $PORT --timeout 600 app:app
