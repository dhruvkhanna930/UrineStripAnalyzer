// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ImageUpload from './components/ImageUpload';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<ImageUpload />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
