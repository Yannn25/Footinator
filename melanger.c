#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHAR 1024

int main(int argc, char* argv[]) {
  char chaine[MAX_CHAR], tmp[MAX_CHAR];
  FILE* fichier = NULL;
  FILE* fichier2 = NULL;
  int i, aleat;

  if (argc < 3) {
    printf("Usage : %s fichierEntree fichierSortie\n", argv[0]);
    return 1;
  }

  fichier = fopen(argv[1], "r");
  fichier2 = fopen(argv[2], "w");

  if (fichier == NULL) {
    printf("Impossible d'ouvrir le fichier %s\n", argv[1]);
    return 1;
  }
  if (fichier2 == NULL) {
    printf("Impossible de creer le fichier %s\n", argv[2]);
    return 1;
  }

  while (fgets(chaine, MAX_CHAR, fichier) != NULL) {
    strcpy(tmp, chaine);
    aleat = rand() % 2;
    if (aleat == 0) {
      fputs(chaine, fichier2);
    } else if (aleat == 1) {
      for (i = strlen(tmp) - 1; i >= 0; i--) {
        chaine[strlen(tmp) - 1 - i] = tmp[i];
      }
      fputs(chaine, fichier2);
    }
  }

  fclose(fichier);
  fclose(fichier2);

  return 0;
}