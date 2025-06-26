CREATE TABLE states (
  id INT PRIMARY KEY,
  name VARCHAR(256)
);

CREATE TABLE cities (
  id INT PRIMARY KEY,
  state_id INT,
  name VARCHAR(256),
  FOREIGN KEY (state_id) REFERENCES states(id)
);
