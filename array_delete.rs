impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut i = 0;
        while i < nums.len() {
            if nums[i] == val {
                for j in i..nums.len()-1 {
                    nums[j] = nums[j+1];
                }
                nums.truncate(nums.len()-1)                
            } else {
                i+=1            
            }
        }
        return nums.len() as i32
    }
}
