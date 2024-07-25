require 'webrick'

# Define a new server on port 8000
server = WEBrick::HTTPServer.new(Port: 8000)

# Mount a root route
server.mount_proc '/' do |req, res|
  res.body = 'Hello, World!'
end

# Trap signals to gracefully shut down the server
trap 'INT' do
  server.shutdown
end

# Start the server
server.start
