create table category
(
    id   serial
        primary key,
    name varchar(50)
);

alter table category
    owner to gabriel;

