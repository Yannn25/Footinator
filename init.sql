CREATE TABLE joueurs(j_id SERIAL PRIMARY KEY, 
nom VARCHAR(50) NOT NULL, 
age INTEGER NOT NULL, 
equipe_nationale VARCHAR(50) NOT NULL, 
championnat VARCHAR(50) NOT NULL, 
poste VARCHAR(50) NOT NULL);

CREATE TABLE questions (q_id SERIAL PRIMARY KEY, question VARCHAR(150) NOT NULL);
INSERT INTO questions(question,liaison) VALUES ('le joueur est-il d''origine ','equipe_nationale');
INSERT INTO questions(question,liaison) VALUES ('le joueur a-il plus de ','age');
INSERT INTO questions(question,liaison) VALUES ('le joueur a-il moins de ','age');
INSERT INTO questions(question,liaison) VALUES ('le joueur joue t''il dans l''équipe nationale ','equipe_nationale');
INSERT INTO questions(question,liaison) VALUES ('le joueur joue t''il dans un ','championnat');
INSERT INTO questions(question,liaison) VALUES ('le joueur joue t''il au poste ','poste');

