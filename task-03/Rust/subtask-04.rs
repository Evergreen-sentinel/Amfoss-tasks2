use std::fs;

fn print_star_pattern(n: usize) -> String {
    let mut pattern = String::new();

    for i in (1..=n).step_by(2) {
        let spaces = (n - i) / 2;
        pattern.push_str(&" ".repeat(spaces)); 
        pattern.push_str(&"*".repeat(i)); 
        pattern.push('\n'); 
    }

    for i in (1..n).rev().step_by(2) {
        let spaces = (n - i) / 2;
        pattern.push_str(&" ".repeat(spaces)); 
        pattern.push_str(&"*".repeat(i)); 
        pattern.push('\n'); 
    }

    pattern
}

fn main() -> std::io::Result<()> {
    let input = fs::read_to_string("input2.txt")?;
    let s: usize = input.trim().parse().expect("Please enter a valid number");

    let pattern = print_star_pattern(s);

    fs::write("output2.txt", pattern)?;

    Ok(())
}
