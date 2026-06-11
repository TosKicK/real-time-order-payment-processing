function StatsCards({ stats }) {
  return (
    <div className="cards">
      <div className="card total">
        <h3>Total Events</h3>
        <p>{stats.total || 0}</p>
      </div>

      <div className="card matched">
        <h3>Matched</h3>
        <p>{stats.matched || 0}</p>
      </div>

      <div className="card discarded">
        <h3>Discarded</h3>
        <p>{stats.discarded || 0}</p>
      </div>

      <div className="card expired">
        <h3>Expired</h3>
        <p>{stats.expired || 0}</p>
      </div>
    </div>
  );
}

export default StatsCards;