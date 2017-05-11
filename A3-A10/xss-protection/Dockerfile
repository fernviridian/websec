FROM node:4
RUN npm install express

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY xss_server.js /usr/src/app/

EXPOSE 1234

CMD [ "node", "/usr/src/app/xss_server.js" ]
