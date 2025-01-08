use std::env::args;



fn main() {
    let n = args().nth(1).expect("need one argument")
        .parse().expect("not an integer");
    println!("{}", factorial(n));    
}
fn factorial_tail(n: u64, acc: u64) -> u64 {
    if n == 0 {
        acc
    } else {
        factorial_tail(n - 1, n * acc)
    }
}

fn factorial(n: i64) -> u64 {
    let abs_n = n.abs() as u64;
    factorial_tail(abs_n, 1)
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_factorial() {
        assert_eq!(factorial(0), 1);
        assert_eq!(factorial(1), 1);
        assert_eq!(factorial(2), 2);
        assert_eq!(factorial(3), 6);
        assert_eq!(factorial(4), 24);
        assert_eq!(factorial(5), 120);
        assert_eq!(factorial(6), 720);
        assert_eq!(factorial(7), 5040);
        assert_eq!(factorial(8), 40320);
        assert_eq!(factorial(9), 362880);
        assert_eq!(factorial(10), 3628800);
        assert_eq!(factorial(-1), 1);
        assert_eq!(factorial(-10), 3628800);
       
        
    }
}

