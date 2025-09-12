impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut i: usize = 0;
        let mut j: usize = height.len() - 1;
        let mut best: i32 = 0;

        while i < j {
            let cur_h = if height[i] < height[j] { height[i] } else { height[j] };
            let area = cur_h * (j - i) as i32;

            while i < j && height[i] <= cur_h {
                i += 1;
            }
            while i < j && height[j] <= cur_h {
                j -= 1;
            }

            if area > best {
                best = area;
            }
        }

        best
    }
}