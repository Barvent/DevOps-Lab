# DevOps-Lab
Simple laboratory to try DevOps concepts

# Machine list
For now there are the following machines in the network:
Machine |   Service |   IP
linuxtemplate   |   Template    |   10.0.3.2
web1    |   Serve a webapp    | 10.0.3.10

# Networking documentation
Use netplan to change the network configuration.
```
network:
    ethernets:
        enp0s3:
        dhcp4: false
        addresses:
        -   10.0.3.2/24
        gateway4: 10.0.3.1
        nameservers
            addresses: [8.8.8.8]
    version: 2
```
Then run:
```bash
sudo netplan try
sudo netplan apply
```

# Manual installation (without Docker and Gunicorn)
The installation of the webapp is done using pipenv
```
pip install pipenv
cd webapp
pipenv install
pipenv run flask --app wsgi run
```
# Docker installation
```
sudo docker build -t webapp .
sudo docker run --name webapp --rm -p 5000:5000 -it webapp
```
