FROM node:4
RUN npm install express request

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY csp_server.js /usr/src/app/

EXPOSE 1234 4321

CMD [ "node", "/usr/src/app/csp_server.js" ]
