const fs = require('fs');

// Charger les données des joueurs
let playersData = fs.readFileSync('final_players.csv', 'utf-8');

// Convertir les données CSV en tableau d'objets
let players = playersData.split('\n').map(player => {
  let [name,club,nationality,lieu_naissance,age,poste,position,pied,taille,valeur,championnat] = player.split(',');
  return {name,club,nationality,lieu_naissance,age,poste,position,pied,taille,valeur,championnat};
});

// Fonction de filtrage pour les joueurs (expression de fonction)
const filterPlayers = function(players, filters) {
  return players.filter(player => {
    let match = true;
    for (let filter in filters) {
      if (filters[filter] !== '' && player[filter] !== filters[filter]) {
        match = false;
      }
    }
    return match;
  });
};

// Exemple d'utilisation du filtre pour trouver les attaquants français
let filters = { poste: 'Attack', nationality: 'France' };
let filteredPlayers = filterPlayers(players, filters);

// Afficher les résultats de la recherche
console.log(filteredPlayers);
