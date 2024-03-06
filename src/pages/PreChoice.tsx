import { Button, Input } from "@nextui-org/react";
import { useState } from "react";

const API_URL = "http://localhost:8000";

export const PreChoice = () => {
  let [lat, setLat] = useState(0);
  let [long, setLong] = useState(0);
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;
      setLat(latitude);
      setLong(longitude);
      console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
    });
  } else {
    console.log("Geolocation is not supported by this browser.");
  }
  let sendCoords = async () => {
    //placeholder
    console.log("sending coordinates to backend...")
  };
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      {lat ? (
        <p>
          Looking for restaurants nearby......
          <br />
          Your coordinates are:
          <br />
          {`Latitude: ${lat}, Longitude: ${long}`}
          <br />
          <Button onClick={() => sendCoords()}>OK</Button>
        </p>
      ) : (
        <div>
          Cannot find your location. Input some nearby restaurants:
          <br />
          <Input />
        </div>
      )}
    </div>
  );
};
