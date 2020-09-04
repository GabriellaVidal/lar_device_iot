*device*
sudo chmod -R 777 /dev/ttyUSB0
ampy --port /dev/ttyUSB0 ls
screen /dev/ttyUSB0 115200

*frontend*
npm start
nodemon start

*api*
nodemon src/index.js
service mongod status/start/stop