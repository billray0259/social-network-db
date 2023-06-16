# #!/bin/bash

# # Navigate to the directory containing your app
# cd "$(dirname "$0")"

# # Set PYTHONPATH to include the current directory
# export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# # Start the application
# python -m social_network_db.app


#!/bin/bash
export FLASK_APP="app.py"
export FLASK_ENV="development"
export PYTHONPATH="$PWD/src:$PYTHONPATH"
flask run
