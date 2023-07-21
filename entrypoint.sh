
# entrypoint.sh

#!/bin/bash

gunicorn -k uvicorn.workers.UvicornWorker --port $PORT app:app
