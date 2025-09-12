impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut i = 0;
        let mut cur_c: char;

        let mut iterators: Vec<std::str::Chars> = strs.iter().map(|s| s.chars()).collect();

        loop {
            if let Some(c) = iterators[0].next() {
                cur_c = c;
            } else {
                return strs[0][..i].to_string();
            }
            for it in iterators.iter_mut().skip(1) {
                match it.next() {
                    Some(c) => {
                        if cur_c != c {
                            return strs[0][..i].to_string();
                        }
                    }
                    None => {
                        return strs[0][..i].to_string();
                    }
                }
            }
            i += 1;
        }
    }
}


// Old solution
// impl Solution {
//     pub fn longest_common_prefix(strs: Vec<String>) -> String {
//         let min_length = strs.iter().map(|str| str.len()).min().unwrap();

//         let str_bytes = strs.iter().map(|str| str.as_bytes());
//         let str_bytes: Vec<_> = str_bytes.collect();

//         for index in 0..min_length {
//             let char = str_bytes[0][index];
//             for &str_byte in str_bytes.iter().skip(1) {
//                 if char != str_byte[index] {
//                     return strs[0][..index].to_string();
//                 }
//             }
//         }

//         strs[0][..min_length].to_string()
//     }
// }
