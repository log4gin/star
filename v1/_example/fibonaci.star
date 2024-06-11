def fibonaci (n){
    if lt (n,1){
        1
    }else{
        add (
            fibonaci(sub (n,1))
            fibonaci(sub (n,2))
        )
    }
}


print(now())

a := fibonaci(25)

print(a)

print(now())
