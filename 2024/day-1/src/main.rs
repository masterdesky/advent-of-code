use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    let path = Path::new("../data/input.txt");
    let file = File::open(&path)?;
    let reader = io::BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        let columns: Vec<&str> = line.split_whitespace().collect();
        if columns.len() == 2 {
            let col1: i32 = columns[0].parse().unwrap();
            let col2: i32 = columns[1].parse().unwrap();
            println!("Column 1: {}, Column 2: {}", col1, col2);
        }
    }

    Ok(())
}
