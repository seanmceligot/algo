pub fn minfree_brute(values: &[u32]) -> Option<u32> {
    let values_len = values.len(); 
    let len_bound = values_len - 1;
    for x in 0..len_bound {
        if not_in_list(x as u32, values) {
            return Some(x as u32);
        }
    }
    None
}
pub fn minfree_cached(values: &[u32]) -> Option<u32> {
    let n = values.len();
    let mut taken_cache = vec![false; n + 1];
    let n_unsigned = n as u32;
    // Initialize F with all False values. For every number x in A, mark the flag F [x] true if
    // x < n. 
    for x in values.iter() {
        if *x < n_unsigned {
            taken_cache[*x as usize] = true;
        }
    }
    // Finally, scan F to find the first false flag. This program takes time proportion to
    // n. It uses the (n + 1)-th flag to cover the special case of sort(A) = [0, 1, 2, . . . , n − 1]. 
    // for i ← 0 to n do
    for (i, is_taken) in taken_cache.iter().enumerate() {
        if !is_taken {
            return Some(i as u32)
        }
    }
    None
}
fn not_in_list(x: u32, list: &[u32]) -> bool {
    for i in 0..list.len() - 1 {
        if x == list[i] {
            return false;
        }
    }
    true
}

// test minfree_brute

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_minfree_brute() {
        // create a scrambled order array with a 0 through 8 and 10 through 20 but no 9
        let taken = [8, 7, 2, 4, 12, 10, 11, 3, 0, 1, 5, 6, 13, 14, 15, 16, 17, 18, 19, 20];
        assert_eq!(minfree_brute(&taken).unwrap(), 9);
    }

    // test minfree_cached
    #[test]
    fn test_minfree_cached() {
        // create a scrambled order array with a 0 through 8 and 10 through 20 but no 9
        let taken = [8, 7, 2, 4, 12, 10, 11, 3, 0, 1, 5, 6, 13, 14, 15, 16, 17, 18, 19, 20];
        assert_eq!(minfree_cached(&taken).unwrap(), 9);
    }
}
