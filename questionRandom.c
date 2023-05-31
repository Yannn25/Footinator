#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int numOfLIne(char* name) {
  int count = 0;
  char c;
  FILE* f = fopen(name, "r");
  if (f == NULL) {
    perror("erreur lors de l'ouverture du fichier\n");
  }
  while ((c = getc(f)) != EOF) {
    if (c == '\n') {
      count++;
    }
  }
  fclose(f);
  return count;
}

int nombreRandom(int n) {
  int nombre;
  nombre = rand() % (n + 1);
  return nombre;
}
// choisi aléatoirement le fichier dans laquelle la question sera posée
char* fichierQuestionRandom() {
  int nombre;
  nombre = rand() % 5; // car il y a 5 catégaries

  if (nombre == 0) {
    return "questionAge.txt";
  } else if (nombre == 1) {
    return "questionClub.txt";
  } else if (nombre == 2) {
    return "questionLieu.txt";
  } else if (nombre == 3) {
    return "questionOrigine.txt";
  } else {
    return "questionPeau.txt";
  }
}
// affiche de manière aléatoire des questions à partir des 5 fichiers de
// questions
char* afficheQuestionRandom() {
  char* file = fichierQuestionRandom();
  FILE* ptr = fopen(file, "r"); // j'ouvre le fichier de question de manière
                                // random parmi les 5 categories
  int randomLIne = nombreRandom(numOfLIne(file));
  char* ligne = malloc(sizeof(1000));

  if (ptr == NULL) {
    perror("erreur lors de l'ouverture du fichier\n");
  }

  for (int i = 0; i <= randomLIne; i++) {
    fgets(ligne, 1000, ptr);
  }
  return ligne;
  fclose(ptr);
}
