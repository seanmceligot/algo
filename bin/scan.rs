fn main() {
    let v = vec![1, 2, 3];
    let sc = v
        .iter()
        .scan(0, |a: &mut i32, b: &i32| {
            *a += b;
            Some(*a)
        })
        .collect::<Vec<_>>();
    println!("v: {:?}", v);
    println!("sc: {:?}", sc);
}
