// src/CoverLetter.js

import React, { useEffect, useState } from 'react';
import { useLocation, Link } from 'react-router-dom';

export default function CoverLetter() {
  const [letter, setLetter] = useState('');
  const [job, setJob] = useState({});
  const [match, setMatch] = useState(0);
  const query = new URLSearchParams(useLocation().search);
  const jobId = query.get('job_id');

  
  useEffect(() => {
    async function fetchLetter() {
      try {
        const resp = await fetch('/api/cover-letter', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ jobId })
        });
        const { letter, job, match } = await resp.json();
        setLetter(letter);
        setJob(job);
        setMatch(match);
      } catch (err) {
        console.error('Error fetching cover letter:', err);
      }
    }
    if (jobId) fetchLetter();
  }, [jobId]);

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      {/* Job Title + Match Bar */}
      <h2 className="text-2xl font-semibold text-center text-indigo-700 mb-2">
        {job.title} @ {job.company?.name}
      </h2>
      <div className="w-full bg-gray-200 rounded-full h-4 mb-1">
        <div
          className="bg-indigo-500 h-4 rounded-full transition-width"
          style={{ width: `${match}%` }}
        />
      </div>
      <p className="text-center text-sm text-gray-600 mb-6">
        {match}% Match
      </p>

      {/* Generated Cover Letter */}
      <div className="bg-white rounded-2xl shadow p-6">
        <pre className="whitespace-pre-wrap text-gray-800">{letter}</pre>
      </div>

      {/* Back Link */}
      <div className="mt-4 text-center">
        <Link to="/" className="text-indigo-500 hover:underline">
          ← Back to Jobs
        </Link>
      </div>
    </div>
  );
}
