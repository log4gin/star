// logic bool //
_true := true 
_false := false
print(_true,_false)

// string //
_string := 'i am a string'
print(_string)

// int //
_int := 2024
print(_int)

// float //
_float := 2.33333333333333
print(_float)

def m (a){
    print(a)
}

// table //
_table := table('first','second','and more',m,_true)
print(_table)

table_set(_table,'name','gin')
print(table_get(_table,'name'))




// _table[0] = 1
// _table[name] = 'sss'
