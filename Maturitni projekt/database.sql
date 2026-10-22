-- 1. Tabulka pro uživatele
CREATE TABLE uzivatele (
    id_uzivatele INT AUTO_INCREMENT PRIMARY KEY,
    uzivatelske_jmeno VARCHAR(50) NOT NULL,
    heslo VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);

-- 2. Tabulka pro obtížnost hry
CREATE TABLE obtiznost (
    id_obtiznosti INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(50) NOT NULL
);

-- 3. Propojovací tabulka pro skóre (vazba 1:N na uživatele i obtížnost)
CREATE TABLE skore (
    id_skore INT AUTO_INCREMENT PRIMARY KEY,
    id_uzivatele INT NOT NULL,
    id_obtiznosti INT NOT NULL,
    body INT NOT NULL,
    datum DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_uzivatele) REFERENCES uzivatele(id_uzivatele),
    FOREIGN KEY (id_obtiznosti) REFERENCES obtiznost(id_obtiznosti)
);