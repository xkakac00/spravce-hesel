/* Vytvoření databáze password_manager */
CREATE DATABASE password_manager;
/* Použití databáze */
USE password_manager;

/* Vytvoření tabulky users */
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY, /* Primarní klíč, autentické navyšování */
    full_name VARCHAR(100) NOT NULL,   /* Celé jméno uživatele */
    user_name VARCHAR(100) NOT NULL,   /* Uživatelské jméno */
    user_password VARCHAR(100) NOT NULL /* Heslo uživatele */
); 

/* Vytvoření tabulky passwords */
CREATE TABLE passwords(
    id INT AUTO_INCREMENT PRIMARY KEY, /* Primární klíč, autentické navyšování */
    user_id INT NOT NULL, /* Cizí klíč, odkazuje na id v tabulce users */
    service_name VARCHAR(255) NOT NULL, /* Název služby */
    user_name VARCHAR(255) NOT NULL, /* Uživatelské jméno pro danou službu */
    user_password VARCHAR(255) NOT NULL, /* Heslo pro danou službu */
    FOREIGN KEY (user_id) REFERENCES users(id) /* Definice cizího klíče */
);
