import "dotenv/config";

import fetch from "node-fetch";
export function getRecentTweets(params) {
    // curl "https://api.twitter.com/2/tweets/search/recent?query=%22ich%20habe%20keine%20zeit%22" -H "Authorization: Bearer $BEARER_TOKEN"
    const url = new URL("https://api.twitter.com/2/tweets/search/recent");
    for (let param in params) {
        url.searchParams.append(param, params[param]);
    }
    return fetch(url, {
        headers: { Authorization: `Bearer ${process.env.TOKEN}` },
    });
}

export function getAllTweets(params) {
    // curl "https://api.twitter.com/2/tweets/search/all?query=%22ich%20habe%20keine%20zeit%22&start_time=2006-01-01T00:00:00.000Z&end_time=2022-03-01T00:00:00.000Z" -H "Authorization: Bearer $BEARER_TOKEN"
}
