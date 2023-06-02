#include "header.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void afficheHomePage() {
  printf("BIENVENU SUR "
         "FOOTINATOR!!!\n\na.Jouer\n\nb.Comment-jouer\n\nc.A-propos\n\na  b  "
         "c ?\n\n");
}

void afficheChoice() {
  char* question = afficheQuestionRandom();
  printf("%s\na.Oui\nb.Non\na  b ?\n\n", question);
}

void afficheCommentjouer() { // À completer plus tard
  printf("Pour jouer à ce jeu......\n\n");
};

void afficheApropos() {
  printf("Ce projet a était réalisé par Yann Edikeu ainsi que Olivier Manyim "
         "pour le projet de Linguistique Informatique\n Voici nos ID :\n "
         "Olivier Manyim : 21959946\n Yann Edikeu : xxxxxxx\n\n");
}

void afficheMessagederetour() {
  printf("Pour retourner à la page d'acceuil taper a\n\n");
}
void interact(char c) {
  char str[100];
  // h pour homepage
  if (c == 'h') {
    afficheHomePage();
    while (1) {
      scanf("%s", str);
      if (strcmp(str, "a") == 0) {
        afficheChoice();
      } else if (strcmp(str, "b") == 0) {
        afficheCommentjouer();
      } else if (strcmp(str, "c") == 0) {
        interact('a');
      } else {
        afficheHomePage();
      }
    }
  }
  // gestion de la page à-propos
  if (c == 'a') {
    afficheHomePage();
    afficheMessagederetour();
  }
}

int main() {
  srand(time(NULL));
  interact('h');
  // afficheChoice();
  return 0;
}