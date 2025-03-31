// compress.js
// This script compresses the selected JSON file using fflate and downloads the archive.

function compressJsonFile() {
    const input = document.getElementById("jsonInput");
    if (input.files.length === 0) {
      alert("Please select a JSON file to compress.");
      return;
    }
    
    const file = input.files[0];
    const reader = new FileReader();
    
    reader.onload = function(e) {
      // Read the file as text
      const jsonText = e.target.result;
      // Convert the text to a Uint8Array
      const encoder = new TextEncoder();
      const jsonBytes = encoder.encode(jsonText);
      
      // Compress using fflate's deflateSync.
      // Using level: 1 prioritizes speed over compression ratio.
      const compressed = fflate.deflateSync(jsonBytes, { level: 1 });
      
      // Create a Blob from the compressed data and trigger a download.
      const blob = new Blob([compressed], { type: "application/octet-stream" });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      // Use a custom extension (e.g., .fzip) for your compressed file.
      link.download = file.name + ".fzip";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    };
    
    // Read the file as text (since it's JSON)
    reader.readAsText(file);
  }