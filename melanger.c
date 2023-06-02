#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int numOfLIne(char* fi) {
  int count = 0;
  char c;
  FILE* f = fopen(fi, "r");
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
  srand(time(NULL));
  return nombre;
}

void swapLines(char* fileName, int line1, int line2) {
  FILE* file1;

  // Ouverture du fichier
  file1 = fopen(fileName, "r");

  // Déclaration des variables
  char line1Data[100], line2Data[100];
  int i;

  // Déplacement du curseur
  for (i = 1; i < line1; i++)
    fgets(line1Data, 100, file1);
  for (i = 1; i < line2; i++)
    fgets(line2Data, 100, file1);
  fclose(file1);

  // Ouverture du fichier
  file1 = fopen(fileName, "w");

  // Déplacement du curseur
  for (i = 1; i < line1; i++)
    fprintf(file1, "%s", line2Data);
  for (i = 1; i < line2; i++)
    fprintf(file1, "%s", line1Data);
  fclose(file1);
}

int main() {
  // je swap aléatoirement 70 lignes
  /*for (int i = 0; i < 2; i++) {
    int l1 = nombreRandom(numOfLIne("question.txt"));
    int l2 = nombreRandom(numOfLIne("question.txt"));
    swapLines("question.txt", l1, l2);
  }*/
  int l1 = nombreRandom(numOfLIne("question.txt"));
  int l2 = nombreRandom(numOfLIne("question.txt"));
  swapLines("question.txt", l1, l2);
  printf(" numofline = %d l1 = %d l2= %d\n", numOfLIne("question.txt"), l1, l2);

  return 0;
}