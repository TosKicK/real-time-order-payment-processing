function EventsTable({ events }) {
  return (
    <div className="table-container">
      <h2>Processed Events</h2>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Order ID</th>
            <th>Order Time</th>
            <th>Payment Time</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {events.map((event) => (
            <tr key={event[0]}>
              <td>{event[0]}</td>
              <td>{event[1]}</td>
              <td>{event[2]}</td>
              <td>{event[3] || "N/A"}</td>

              <td>
                <span className={`status ${event[4].toLowerCase()}`}>
                  {event[4]}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EventsTable;