CREATE TABLE LesSportifs_base
(
  numSp NUMBER(4),
  nomSp VARCHAR2(20),
  prenomSp VARCHAR2(20),
  pays VARCHAR2(20),
  categorieSp VARCHAR2(10),
  dateNaisSp DATE,
  CONSTRAINT SP_PK PRIMARY KEY(numSp),
  CONSTRAINT SP_CK1 CHECK(numSp > 0),
  CONSTRAINT SP_UN UNIQUE(nomSp, prenomSp),
  CONSTRAINT SP_CK2 CHECK(categorieSp IN ('feminin','masculin'))
);

CREATE TABLE LesEquipiers
(
  numEq NUMBER(4) NOT NULL,
  numSp NUMBER(4) NOT NULL,
  CONSTRAINT EQ_PK PRIMARY KEY(numEq, numSp),
  CONSTRAINT EQ_FK FOREIGN KEY(numSp) REFERENCES LesSportifs_base(numSp),
  CONSTRAINT EQ_CK1 CHECK(numEq > 0)
);

CREATE TABLE LesEpreuves
(
  numEp NUMBER(3),
  nomEp VARCHAR2(20),
  formeEp VARCHAR2(13),
  categorieEp VARCHAR2(10),
  nbSportifsEp NUMBER(2),
  dateEp DATE,
  nomDi VARCHAR2(20),
  CONSTRAINT EP_PK PRIMARY KEY (numEp),
  CONSTRAINT EP_CK1 CHECK (formeEp IN ('individuelle','par equipe','par couple')),
  CONSTRAINT EP_CK2 CHECK (categorieEp IN ('feminin','masculin','mixte')),
  CONSTRAINT EP_CK3 CHECK (numEp > 0),
  CONSTRAINT EP_CK4 CHECK (nbSportifsEp > 0)
);

CREATE TABLE LesInscriptions
(
  numIn NUMBER(4) NOT NULL,
  numEp NUMBER(4) NOT NULL,
  CONSTRAINT I_PK PRIMARY KEY(numIn, numEp),
  CONSTRAINT I_FK FOREIGN KEY(numEp) REFERENCES LesEpreuves(numEp),
  CONSTRAINT I_CK1 CHECK (numIn > 0)
);

CREATE TABLE LesResultats
(
  numEp NUMBER(4),
  gold NUMBER(4),
  silver NUMBER(4),
  bronze NUMBER(4),
  CONSTRAINT RES_PK PRIMARY KEY (numEp),
  CONSTRAINT RES_FK1 FOREIGN KEY (gold, numEp) REFERENCES LesInscriptions(numIn,numEp),
  CONSTRAINT RES_FK2 FOREIGN KEY (silver, numEp) REFERENCES LesInscriptions(numIn,numEp),
  CONSTRAINT RES_FK3 FOREIGN KEY (bronze, numEp) REFERENCES LesInscriptions(numIn,numEp),
  CONSTRAINT RES_CK1 CHECK (gold<>silver AND silver<>bronze AND gold<>bronze)
);

CREATE TABLE LesDisciplines
(
  nomDi VARCHAR2(20),
  CONSTRAINT DI_FK FOREIGN KEY(nomDi) REFERENCES LesEpreuves(nomDi)
);

CREATE VIEW LesSportifs AS
SELECT  numSp,nomSp,prenomSp,pays,categorieSp,dateNaisSp,(strftime('%Y', 'now') - strftime('%Y', dateNaisSp))AS ageSP
FROM LesSportifs_base;

CREATE VIEW LesEquipes AS
SELECT DISTINCT E.numEq as numEq, COUNT(E.numSp) as num, S.pays as pays
FROM LesEquipiers E LEFT OUTER JOIN LesSportifs S ON(E.numSp=S.numSp)
GROUP BY numEq;

CREATE VIEW InsEtPay AS
SELECT DISTINCT pays,numSp as num
FROM LesSportifs
UNION
SELECT DISTINCT pays,numEq as num
FROM LesEquipes;

CREATE VIEW GoldEtPay AS
SELECT COUNT(R.gold) as gold, I.pays as pays
FROM LesResultats R LEFT OUTER JOIN InsEtPay I ON (R.gold=I.num)
GROUP BY pays;

CREATE VIEW SilverEtPay AS
SELECT COUNT(R.silver) as silver, I.pays as pays
FROM LesResultats R LEFT OUTER JOIN InsEtPay I ON (R.silver=I.num)
GROUP BY pays;

CREATE VIEW BronzeEtPay AS
SELECT COUNT(R.bronze) as bronze, I.pays as pays
FROM LesResultats R LEFT OUTER JOIN InsEtPay I ON (R.bronze=I.num)
GROUP BY pays;

CREATE VIEW AllPays AS
SELECT DISTINCT pays
FROM LesSportifs_base;



-- TODO 1.2a : ajouter la définition de la vue LesSportifs
-- TODO 1.3a : ajouter la création de la table LesDisciplines et ajouter l'attribut discipline dans la table LesEpreuves
-- TODO 1.4a : ajouter la définition de la vue LesEquipes
