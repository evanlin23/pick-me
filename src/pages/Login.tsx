import { Button, Input, Slider, Checkbox } from "@nextui-org/react";

export default function App() {}

export const Login = () => {
  return (
    <div
      style={{
        justifyContent: "center",
        height: "100%",
        marginLeft: "10vw",
        marginTop: "-10%",
        width: "80vw",
        flexDirection: "column",
        alignSelf: "center"
      }}
      className="space-y-4"
    >
      <h1 style={{ fontSize: "30px" }}>Log in and select your preferences</h1>
      <div className="flex gap-4">
        <Input label="Name" placeholder="Enter your name" />
        <Input type="email" label="Email" placeholder="Enter your email" />
        <Input
          type="password"
          label="Password"
          placeholder="Enter a password"
        />
      </div>
      <h2 style={{fontSize: "20px"}}>What do you plan to use PickMe for?</h2>
      <div className="flex gap-4">
        <Checkbox radius="full">Restaurants</Checkbox>
        <Checkbox radius="full">Something else</Checkbox>
      </div>
      <h2 style={{fontSize: "20px"}}>Rate your preference for the following cuisines:</h2>
      <div>
        <h4>Italian</h4>
        <Slider />
      </div>
      <div>
        <h4>American</h4>
        <Slider />
      </div>
      <div>
        <h4>Indian</h4>
        <Slider />
      </div>
      <div>
        <h4>Middle Eastern</h4>
        <Slider />
      </div>
      <div>
        <h4>Chinese/Korean</h4>
        <Slider />
      </div>
      <div>
        <h4>Fast Food</h4>
        <Slider />
      </div>
      <Button color="primary" style={{ marginTop: "20px" }}>
        Submit Preferences
      </Button>
    </div>
  );
};
