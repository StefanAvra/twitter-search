import "dotenv/config";
import fetch from "node-fetch";
import { getRecentTweets } from "./twitter-api.js";

const response = await getRecentTweets({ query: "ich habe keine zeit" });
const data = await response.json();

console.log(data);
