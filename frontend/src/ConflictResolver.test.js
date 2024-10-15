// src/components/ConflictResolver.js
import React, { useState } from 'react';

const ConflictResolver = () => {
    const [party1Input, setParty1Input] = useState('');
    const [party2Input, setParty2Input] = useState('');
    const [resolution, setResolution] = useState('');

    const handleResolve = () => {
        setResolution(`Compromise reached between: "${party1Input}" and "${party2Input}"`);
    };

    return (
        <div>
            <h2>Conflict Resolution Mediator</h2>
            <div>
                <textarea 
                    placeholder="Party 1's perspective..." 
                    value={party1Input}
                    onChange={(e) => setParty1Input(e.target.value)} 
                />
            </div>
            <div>
                <textarea 
                    placeholder="Party 2's perspective..." 
                    value={party2Input}
                    onChange={(e) => setParty2Input(e.target.value)} 
                />
            </div>
            <button onClick={handleResolve}>Resolve Conflict</button>
            {resolution && <p>{resolution}</p>}
        </div>
    );
};

export default ConflictResolver;
