DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tasks;

CREATE TABLE users (
    id SERIAL NOT NULL UNIQUE,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    avatar TEXT NOT NULL,
    email TEXT NOT NULL,
    username TEXT NOT NULL
);

CREATE TABLE tasks (
    id SERIAL NOT NULL UNIQUE,
    description TEXT NOT NULL,
    status VARCHAR(1000) NOT NULL,
    created TIMESTAMPTZ NOT NULL,
    due_date DATE NOT NULL,
    completed BOOLEAN NOT NULL,
);


