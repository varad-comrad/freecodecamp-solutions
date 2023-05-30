fn fizzbuzz(n: i32, lower: i32, upper: i32) -> Vec<String> {
    let mut ans = Vec::new();
    for i in 1..=n {
        let mut aux = String::new();
        if i%lower == 0 {
            aux.push_str("Fizz");
        }
        if i%upper == 0 {
            aux.push_str("Buzz");
        }
        if i%lower!=0 && i%upper!=0 {
            aux += &i.to_string();
        }
        ans.push(aux);
    }
    ans
}

fn main(){
    println!("{0:?}", fizzbuzz(15, 3, 5));
}