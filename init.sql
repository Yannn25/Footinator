CREATE TABLE joueurs(j_id SERIAL PRIMARY KEY, 
nom VARCHAR(50) NOT NULL, 
age INTEGER NOT NULL, 
equipe_nationale VARCHAR(50) NOT NULL, 
championnat VARCHAR(50) NOT NULL, 
poste VARCHAR(50) NOT NULL);

CREATE TABLE questions (q_id SERIAL PRIMARY KEY, question VARCHAR(150) NOT NULL);
\copy joueurs from 'joueurs.csv' WITH (FORMAT CSV, HEADER);
\copy questions from 'questions.csv' WITH (FORMAT CSV, HEADER);

