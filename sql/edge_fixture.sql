-- Fixture for the incremental-merge subtree test: deleted as a whole later.
CREATE TABLE edge_fixture_sheet (
  sheet_id INT NOT NULL,
  book_name VARCHAR(100) NOT NULL,
  kind VARCHAR(20) NOT NULL DEFAULT 'worksheet',
  row_count INT,
  PRIMARY KEY (sheet_id),
  KEY idx_edge_fixture_book (book_name)
);
