import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/sample/")
            .then((response) => {
                setMessage(response.data.message);
            })
            .catch((error) => console.error("Error fetching data:", error));
    }, []);

    return <h1>This is the message passed via the API: {message}</h1>;
}

export default App;