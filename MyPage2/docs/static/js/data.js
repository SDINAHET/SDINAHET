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
   PLACES (exemple)
------------------------- */
const places = {
    "p1": {
        id: "p1",
        name: "Villa Bretagne",
        location: "Rennes",
        price_per_night: 120,
        description: "Belle maison proche du parc du Thabor."
    },
    "p2": {
        id: "p2",
        name: "Appartement Montfort",
        location: "Montfort-sur-Meu",
        price_per_night: 80,
        description: "Appartement calme et lumineux."
    }
};

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
