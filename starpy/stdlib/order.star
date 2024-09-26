order := table()

order.max = def _ (t) {
    n  := len(t)
    i := 0
    resoult := t[i]
    while (i < n){
        if (t[i] > resoult) {
            resoult = t[i]
        }
        i++
    }
    resoult
}

order.choose = def _ (t){

    // 初始化
    n := len(t)
    i := 0 
    min_idx := i
    j := (i + 1)

    // 逻辑部分
    while (i < n) {
        min_idx = i
        j = ( i + 1 )  
        
        while (j < n) {
            if (t[j] < t[min_idx]) {
                min_idx = j
            }
            j++
        }

        if (min_idx != i) {
            tmp := t[min_idx]
            t[min_idx] = t[i]
            t[i] = tmp
        }
        i++
    }
    t  
}

// 导出为包

order

