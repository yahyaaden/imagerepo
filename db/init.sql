CREATE DATABASE imagerepo;
use imagerepo;

CREATE TABLE birds (
    species varchar(500),
    location varchar(500),
    genus varchar(500),
    diet varchar(500),
    imagelink varchar(1000)
);

INSERT INTO birds
    (species, location, genus, diet, imagelink)
VALUES
    ('Red-bearded bee-eater', 'Southeast Asia', 'Nyctyornis', 'Insects, bees, wasps and hornets', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Nyctyornis_amictus_-_Kaeng_Krachan.jpg/320px-Nyctyornis_amictus_-_Kaeng_Krachan.jpg'),
    ('Blue-bearded bee-eater', 'Southeast Asia', 'Nyctyornis', 'Bees', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Nyctyornis_athertoni_-_Khao_Yai.jpg/320px-Nyctyornis_athertoni_-_Khao_Yai.jpg'),
    ('Little bee-eater', 'Sub-Saharan Africa', 'Merops', 'Insects', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Little_bee-eater_%28Merops_pusillus_argutus%29_Namibia.jpg/390px-Little_bee-eater_%28Merops_pusillus_argutus%29_Namibia.jpg'),
    ('African green bee-eater', 'Africa', 'Merops', 'Insects', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Merops_viridissimus_cleopatra_at_Fayoum%2C_Egypt_1.jpg/320px-Merops_viridissimus_cleopatra_at_Fayoum%2C_Egypt_1.jpg');