var botstatesarray = {
    description: "Un robot qui devine le joueur de football au quel vous pensez",
    etats: {
        start: [
            "Bonjour bienvenue, quelle est le poste de votre joueur ?",
            {Attaquant: "attaquant", Milieu: "milieu", Défenseur: "defenseur", Gardien: "gardien"}
        ],
        
        attaquant: [
             "Vous intéressez-vous à l'anglais ?",
             {oui: "choix_en", non: "start"}
        ],
        
        milieu: [
            "Vous intéressez-vous au français ?",
            {oui: "choix_fr", non: "start"}
        ],
        
        defenseur: [
            "Entendu pour le français ! Voulez-vous recommencer ?",
            {oui: "start", non: "end"}
        ],
        
        choix_en: [
            "Entendu pour l'anglais ! Voulez-vous recommencer ?",
            {oui: "start", non: "end"}
        ],
        end: ["Merci et au revoir !"]
    },
    resume: {
        start__mat_fr: "Vous parlez français",
        start__mat_en: "Vous parlez anglais",
        mat_fr__choix_en: "Vous vous intéressez à l'anglais",
        choix_en__end: "Vous avez terminé l'interaction",
        end: "",
    },
};

