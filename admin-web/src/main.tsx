import React from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

function App() {
  return (
    <main className="container">
      <header><span className="logo">🌱 AgriSmart</span><span>Admin Console</span></header>
      <section className="hero">
        <h1>AgriSmart Control Center</h1>
        <p>Manage farmers, farms, AI predictions and platform services.</p>
      </section>
      <section className="grid">
        {['Users','Farms','Crop Recommendations','Disease Predictions','Yield Predictions','Weather'].map(item => (
          <article className="card" key={item}><h2>{item}</h2><p>Management module ready for API integration.</p></article>
        ))}
      </section>
    </main>
  );
}
createRoot(document.getElementById('root')!).render(<React.StrictMode><App /></React.StrictMode>);
