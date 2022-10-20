create table users
(
    id       serial
        primary key,
    name     varchar(50),
    email    varchar(255)
        unique,
    password varchar(255)
);

alter table users
    owner to gabriel;

