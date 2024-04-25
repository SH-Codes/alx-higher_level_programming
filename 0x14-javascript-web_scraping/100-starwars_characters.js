#!/usr/bin/node

const request = require('request');

const getCharacter = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
};

const getMovieCharacters = async (movieId) => {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
  try {
    const response = await new Promise((resolve, reject) => {
      request(apiUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(JSON.parse(body));
      });
    });

    console.log(`Characters in ${response.title}:`);
    for (const characterUrl of response.characters) {
      const characterName = await getCharacter(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
};

const movieId = process.argv[2];
getMovieCharacters(movieId);
