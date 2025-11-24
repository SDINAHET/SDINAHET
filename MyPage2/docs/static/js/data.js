/* -------------------------
   USERS (login statique)
------------------------- */
const users = {
    "test@hbnb.com": {
        password: "user1234",
        name: "Test User",
        id: "u1"
    }
};

/* -------------------------
   LISTE DES PLACES
------------------------- */

const places = [
    {
        id: "p1",
        name: "Appartement Rennes",
        city: "Rennes",
        host: "test@hbnb.com",
        price: 75,
        guests: 2,
        bedrooms: 1,
        bathrooms: 1,
        description: "Petit appartement cosy proche du métro et du centre.",
        image: "static/images/pic-work-01.jpg"
    },
    {
        id: "p2",
        name: "Villa Côtes-d'Armor",
        city: "Plouha",
        host: "test@hbnb.com",
        price: 140,
        guests: 6,
        bedrooms: 3,
        bathrooms: 2,
        description: "Superbe villa avec vue mer.",
        image: "static/images/oldhome.png"
    },
    {
        id: "p3",
        name: "Studio Montfort-sur-Meu",
        city: "Montfort",
        host: "test@hbnb.com",
        price: 59,
        guests: 1,
        bedrooms: 1,
        bathrooms: 1,
        description: "Studio parfait pour un étudiant ou un week-end calme.",
        image: "static/images/logo.png"
    }
];


/* -------------------------
   REVIEWS (liées aux places)
------------------------- */
const reviews = [
    {
        place_id: "p1",
        user_id: "u1",
        comment: "Super week-end, très propre et calme !",
        rating: 5
    },
    {
        place_id: "p1",
        user_id: "u1",
        comment: "Wifi un peu lent mais hôte sympa.",
        rating: 4
    },
    {
        place_id: "p2",
        user_id: "u1",
        comment: "Très bon rapport qualité/prix.",
        rating: 4
    }
];

/* -------------------------
   LOGIN
------------------------- */
function login(email, password) {
    const user = users[email];

    if (!user) {
        return { success: false, message: "User not found" };
    }

    if (user.password !== password) {
        return { success: false, message: "Wrong password" };
    }

    // Stocker dans le localStorage
    localStorage.setItem("hbnb_user", JSON.stringify(user));

    return { success: true, user };
}

/* -------------------------
   GET CURRENT USER
------------------------- */
function getCurrentUser() {
    const u = localStorage.getItem("hbnb_user");
    return u ? JSON.parse(u) : null;
}
