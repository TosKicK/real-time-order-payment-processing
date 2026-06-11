import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

import { Pie } from "react-chartjs-2";

ChartJS.register(
  ArcElement,
  Tooltip,
  Legend
);

function StatusChart({ stats }) {
    if (
  (stats.matched || 0) +
  (stats.discarded || 0) +
  (stats.expired || 0) === 0
) {
  return (
    <div
      style={{
        textAlign: "center",
        padding: "100px",
        fontSize: "20px",
      }}
    >
      No events yet
    </div>
  );
}
  const data = {
    labels: [
      "Matched",
      "Discarded",
      "Expired"
    ],
    datasets: [
      {
        label: "Events",
        data: [
          stats.matched || 0,
          stats.discarded || 0,
          stats.expired || 0
        ],
        backgroundColor: [
          "#2ecc71",
          "#e74c3c",
          "#f39c12"
        ],
        borderWidth: 1
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "bottom"
      }
    }
  };

  return (
    <div
      style={{
        width: "450px",
        margin: "0 auto"
      }}
    >
      <Pie data={data} options={options} />
    </div>
  );
}

export default StatusChart;