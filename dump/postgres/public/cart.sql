create table cart
(
    id           serial
        primary key,
    user_id      integer
        references users
            on delete cascade,
    created_date timestamp
);

alter table cart
    owner to gabriel;

