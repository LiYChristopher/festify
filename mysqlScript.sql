CREATE DATABASE festify;
use festify;
CREATE TABLE sessions (
    festivalId int(10) NOT NULL AUTO_INCREMENT,
    festivalName varchar(100) NOT NULL,
    userId varchar(30) NOT NULL,
    playlistId varchar(30) NOT NULL,
    playlistURL varchar(512) NOT NULL,
    catalogId varchar(30) NOT NULL,
    urlSlug varchar (512) NOT NULL,
    PRIMARY KEY (festivalId)
);
CREATE table contributors (
    festivalId int (10) NOT NULL,
    userId varchar(30) NOT NULL,
    ready boolean DEFAULT 0 NOT NULL,
    CONSTRAINT FOREIGN KEY (festivalId) REFERENCES sessions(festivalId)
        ON DELETE CASCADE
);
CREATE table parameters (
    festivalId int (10) NOT NULL,
    userId varchar(30) NOT NULL,
    hotness decimal(4,3),
    danceability decimal(4,3),
    energy decimal(4,3),
    variety decimal(4,3),
    genre varchar(30),
    CONSTRAINT FOREIGN KEY (festivalId) REFERENCES contributors (festivalId)
        ON DELETE CASCADE
);
