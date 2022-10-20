create table cart_items
(
    id           serial
        primary key,
    cart_id      integer
        references cart
            on delete cascade,
    product_id   integer
        references products
            on delete cascade,
    created_date timestamp
);

alter table cart_items
    owner to gabriel;

