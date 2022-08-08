# Reservation service
Django bankend service 

## To start the application 
    
### create an environment 
    make venv 
    source venv/bin/activate
or 

    python -m venv venv 
    source venv/bin/activate (different for windows) 
    python -m pip install -r requirements.txt 
    
### Start the application 
    python manage.py runserver <<port>> (or you can use default port)

For local development run the docker compose file

    docker-compose up

above command will start the docker for web and postgres and you can access django on `localhost:8000`.

## Other commands 

To check and fixing formatting

    pre-commit run --all-files

To upgrading requirements.txt or requirements-dev.txt
    
    make -B requirements.txt (or requirements-dev.txt)

You can access the admin on /admin/. To create superuser you might need to run. 
        
    docker exec -it <container_id> /bin/bash 
    python manage.py createsuperuser
