create table products
(
    id          serial
        primary key,
    name        varchar(50),
    quantity    integer,
    description text,
    price       double precision,
    category_id integer
        references category
            on delete cascade
);

alter table products
    owner to gabriel;

