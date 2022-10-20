create table "order"
(
    id               serial
        primary key,
    order_date       timestamp,
    order_amount     double precision,
    order_status     varchar,
    shipping_address text,
    customer_id      integer
        references users
            on delete cascade
);

alter table "order"
    owner to gabriel;

