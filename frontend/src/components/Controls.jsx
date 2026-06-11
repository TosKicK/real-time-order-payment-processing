import API from "../services/api";

function Controls() {
  const sendOrder = async () => {
    const id = Math.floor(Math.random() * 10000);

    try {
      const res = await API.post(`/order?order_id=${id}`);

      console.log(res.data);
      alert(`Order ${id} created successfully`);
    } catch (err) {
      console.error(err);
      alert("Failed to create order");
    }
  };

  const sendPayment = async () => {
    const id = prompt("Enter Order ID");

    if (!id) return;

    try {
      const res = await API.post(`/payment?order_id=${id}`);

      console.log(res.data);
      alert(`Payment sent for Order ${id}`);
    } catch (err) {
      console.error(err);
      alert("Failed to send payment");
    }
  };

  return (
    <div className="controls">
      <button className="btn order-btn" onClick={sendOrder}>
        Generate Order
      </button>

      <button className="btn payment-btn" onClick={sendPayment}>
        Generate Payment
      </button>
    </div>
  );
}

export default Controls;