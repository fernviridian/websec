// Simple web server using JavaScript express
// Takes two URL parameters user and xss
//   xss specifies what the X-XSS-Protection: header on the server should be
//   user is what is echoed back in the reponse
var express = require('express')
var app = express()
app.use((req, res) => {
  if (req.query.xss) res.setHeader('X-XSS-Protection', req.query.xss)
    res.send(`<h1>Hello, ${req.query.user || 'anonymous'}</h1>`)
  console.log(req.url)
 }
)

app.listen(1234)
