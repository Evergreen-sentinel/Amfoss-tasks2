use std::fs;

fn main() {

    let input = fs::read_to_string("input.txt")
        .expect("Failed to read input.txt");

    fs::write("output.txt", input)
        .expect("Failed to write to output.txt");
}
