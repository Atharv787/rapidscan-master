// server.js

const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Sample API route
app.get('/api/status', (req, res) => {
  res.json({ message: 'Server is running!' });
});

// Additional API routes can be defined here

// Serve static files from the front-end
app.use(express.static('public'));

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});