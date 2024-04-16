#!/usr/bin/node
// star wars endpoint

const request = require('request');
const args = process.argv;
const movieId = args[2];
const urlMovie = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(urlMovie, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const charactersUrl = JSON.parse(body).characters;
    charactersUrl.forEach(urlChar => {
      request(urlChar, (error, respond, body) => {
        if (error) {
          console.error('Error:', error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
