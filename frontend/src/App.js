import React, { useState, useEffect } from 'react';

export default function App() {
  const [file, setFile] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetch('/api/jobs')
      .then(res => res.json())
      .then(data => setJobs(data))
      .catch(err => console.error('Error loading jobs from DB:', err));
  }, []);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append('resume', file);

    try {
      const resp = await fetch('/api/refresh-jobs', {
        method: 'POST',
        body: formData
        });
      const data = await resp.json();
      const list =
      Array.isArray(data)
        ? data
        : Array.isArray(data.jobs)
          ? data.jobs
          : [];
      setJobs(list);
    } catch (err) {
      console.error('Error fetching jobs:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold text-center text-indigo-600 mb-8">
        Job Matcher
      </h1>

      <form onSubmit={handleSubmit} className="mb-8 flex flex-col sm:flex-row gap-4">
        <input
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          className="flex-1 p-2 border border-gray-300 rounded"
        />
        <button
          type="submit"
          disabled={loading}
          className="px-4 py-2 bg-indigo-500 text-white rounded hover:bg-indigo-600"
        >
          {loading ? 'Analyzing...' : 'Analyze Resume'}
        </button>
      </form>
      <button
        onClick={async () => {
          setLoading(true);
          await fetch('/api/refresh-jobs', { method: 'POST' });
          const resp = await fetch('/api/jobs');
          const data  = await resp.json();
          const list =
          Array.isArray(data)
            ? data
            : Array.isArray(data.jobs)
              ? data.jobs
              : [];
          setJobs(list);
          setLoading(false);
        }}
        className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600">
        Refresh Jobs
      </button>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {(Array.isArray(jobs) ? jobs : []).map((job) => (
          <div
            key={job.id}
            className="bg-white rounded-2xl shadow p-6 hover:shadow-lg transition-shadow"
          >
            <h2 className="text-xl font-semibold text-indigo-700 mb-2">
              {job.title}
            </h2>
            <p className="text-sm text-gray-600 mb-4">{job.company.name}</p>
            <p className="text-gray-800 mb-4">{job.location}</p>
            <div className="flex justify-between items-center">
              <a
                href={job.url}
                target="_blank"
                rel="noopener noreferrer"
                className="px-4 py-2 bg-indigo-500 text-white rounded-lg hover:bg-indigo-600"
              >
                Apply
              </a>
              <a
                href={`/cover-letter?job_id=${job.id}`}
                className="px-4 py-2 border border-indigo-500 text-indigo-500 rounded-lg hover:bg-indigo-50"
              >
                Cover Letter
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
