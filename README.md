<h1>eeeZeee Server receives and stores sensor data measurements. Python. Sqlite3. Flask APIs. Linux/Win. Docker image.</h1>

<h3>Raspbian Bullseye. Python 3. Minimal demo.</h3> 

<h4>Sensor data acquisition. Flask API exposed at your_IP_address_here:5000/getData</h4> 

<h4>Docker instance:  https://hub.docker.com/r/alfredc333/eeezeee</h4>


<h3>Commands:</h3>

start container in local directory: 
* <b>docker compose up --build</b>

start docker container: 
* <b>docker run -d --name=testserver -p:5000:5000 alfredc333/eeezeee:latest</b>


All files are released under a [MIT license](https://en.wikipedia.org/wiki/MIT_License)
