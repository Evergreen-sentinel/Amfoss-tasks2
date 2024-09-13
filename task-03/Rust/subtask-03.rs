fn print_star_pattern(n: usize) {
    for i in (1..=n).step_by(2) {
        let spaces = (n - i) / 2;
        for _ in 0..spaces {
            print!(" ");
        }
        for _ in 0..i {
            print!("*");
        }
        println!(); 
    }

    for i in (1..n).rev().step_by(2) {
        let spaces = (n - i) / 2;
        for _ in 0..spaces {
            print!(" ");
        }
        for _ in 0..i {
            print!("*");
        }
        println!(); 
    }
}

fn main() {
    let mut input = String::new();
    println!("Enter a number:");
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: usize = input.trim().parse().expect("Please enter a valid number");
    print_star_pattern(n);
}
