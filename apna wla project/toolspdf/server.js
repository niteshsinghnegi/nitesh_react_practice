const express = require("express");
const path = require("path");
const multer = require("multer");

const app = express();
const port = 3000;

// middleware to serve static files
app.use(express.static("public"));

// multer config
const upload = multer({ dest: "uploads/" });

// home route
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// upload route
app.post("/merge", upload.array("pdfs", 10), (req, res) => {
  if (!req.files || req.files.length === 0) {
    return res.send("❌ No PDF selected");
  }

  console.log(req.files);

  res.send("✅ PDF uploaded successfully");
});

// server start
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
