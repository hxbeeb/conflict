// src/App.js
import React from 'react';
import ConflictResolver from './components/ConflictResolver';
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>AI-Powered Conflict Resolution Mediator</h1>
            </header>
            <main>
                <ConflictResolver />
            </main>
        </div>
    );
}

export default App;

