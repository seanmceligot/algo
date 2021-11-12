use std::convert::TryInto;

impl Solution {
    pub fn merge(left: &mut Vec<i32>, m: i32, right: &mut Vec<i32>, n: i32) {
     
        let left_size:usize = m.try_into().unwrap();
        let right_size:usize = n.try_into().unwrap();
        let mut tmp: Vec<i32> = Vec::with_capacity(left_size+right_size);

        let mut lindex:usize = 0;
        let mut rindex:usize = 0;
    
        while (lindex < left_size && rindex < right_size) {
    
            if (left[lindex] <= right[rindex]) {
                tmp.push( left[lindex] );
                lindex+=1;
            } else {
                tmp.push( right[rindex] );
                rindex+=1;            
            }
        }
        while(lindex < left_size) {
                tmp.push( left[lindex] );
                lindex+=1;
        }       
        while(rindex < right_size) {
              tmp.push( right[ rindex ] );
                rindex+=1;
        }
        for i in 0..tmp.len() {
            left[i] = tmp[i];
        }
    }
}
