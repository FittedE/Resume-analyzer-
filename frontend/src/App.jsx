import { useState } from 'react'
import './App.css'

function App() {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    formData.append("file",file);
    formData.append("job_description", jobDescription)
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/analyze",{
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("error fetching data:", error);
    } finally {
      setLoading(false);
    }
    };
    return (
      <>
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={(e)=> setFile(e.target.files[0])}/>
      <textarea value={jobDescription} onChange={(e) => setJobDescription(e.target.value)}/>
      <button type='submit'>Analyze</button>
    </form>
   {result && (
  <div>
    <h2>Match Score:{result.match_score}</h2>

    <h3>Matched Keywords</h3>
    <ul>
      {result.matched_keywords.map((keyword, index) => (
        <li key={index}>{keyword}</li>
      ))}
    </ul>

    <h3>Missing Keywords</h3>
    <ul>
     {result.missing_keywords.map((keyword, index) => (
      <li key={index}>{keyword}</li>
     ))}
    </ul>

    <h3>Strengths</h3>
    <ul>
      {result.strengths.map((strength, index) => (
        <li key={index}>{strength}</li>
      ))}
    </ul>

    <h3>Weaknesses</h3>
    <ul>
      {result.weaknesses.map((weakness, index) => (
        <li key={index}>{weakness}</li>  
   ))}
    </ul>
  </div>
)}
    </>
  );
}
export default App
