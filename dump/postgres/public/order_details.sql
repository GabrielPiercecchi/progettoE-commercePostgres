create table order_details
(
    id         serial
        primary key,
    order_id   integer
        references "order"
            on delete cascade,
    product_id integer
        references products
            on delete cascade,
    quantity   integer,
    created    timestamp
);

alter table order_details
    owner to gabriel;

