import { StatusBar } from "expo-status-bar";
import { useState } from "react";
import { StyleSheet, Text, View, Button } from "react-native";

export default function App() {
  const [counter, setcounter] = useState(0);
  return (
    <View style={styles.container}>
      <Text style={styles.text
      }>Counter : {counter}</Text>
      <View style={styles.buttonContainer}>
        <Button
          title="Increament"
          onPress={() => setcounter((pre) => pre + 1)}
        />
        <Button
          title="Decreament"
          onPress={() => setcounter((pre) => pre - 1)}
        />
      </View>
      {/* <StatusBar style="auto" /> */}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },

  text: {
    fontSize: 24,
    marginBottom: 20,
  },
  buttonContainer: {
    flexDirection: "row",
    justifyContent: "space-around",
    width: "50%",
  },
});
