module.exports = RouteHandler;

function RouteHandler(app, config)
{
  app.get('/', function(req, res)
  {
    res.sendFile("views/index.html");
  });

}
