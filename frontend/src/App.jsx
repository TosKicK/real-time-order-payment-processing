import { useEffect, useState } from "react";
import API from "./services/api";
import StatsCard from "./components/StatsCard";
import EventsTable from "./components/EventsTable";
import StatusChart from "./components/StatusChart";
import Controls from "./components/Controls";
import "./App.css";

function App() {
  const [stats, setStats] = useState({});
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const statsRes = await API.get("/stats");
        const eventsRes = await API.get("/events");

        setStats(statsRes.data);
        setEvents(eventsRes.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();

    const interval = setInterval(fetchData, 3000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="container">
      <h1>🚀 Real-Time Order Payment Dashboard</h1>

      <StatsCard stats={stats} />
      
      <Controls />

      <div className="chart-section">
        <StatusChart stats={stats} />
      </div>

      <EventsTable events={events} />
    </div>
  );
}

export default App;