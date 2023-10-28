# count number of 3.5 players
SELECT COUNT(id) FROM tb_tennis WHERE rating = 3.5;

; average rating of all players
SELECT AVG(rating) FROM tb_tennis;

// between 13-23 years old, with rating 2.3-3.5
SELECT DISTINCT  * FROM tb_tennis WHERE dob > '1990-1-1' AND dob < '2000-12-31' AND rating > 2.5 AND rating < 3.5;


// between 13-23 years old, with rating 2.3-3.5, live in Mountain View
SELECT DISTINCT  * FROM tb_tennis WHERE dob > '1990-1-1' AND dob < '2000-12-31' AND rating > 2.5 AND rating < 3.5 AND city = 'Mountain View';
