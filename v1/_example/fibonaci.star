def fibonaci (n){
    if lt (n,2){
        1
    }else{
         (
            fibonaci((n - 1))
            +
            fibonaci((n - 2))
        )
    }
}


print(now())

times := 0

while lt (times, 15) {
    print(fibonaci(times))
    times++
}

print(now())
