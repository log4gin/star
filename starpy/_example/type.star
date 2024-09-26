// nil
_nil := nil
print(_nil)

// logic bool 
_true := true 
_false := false
print(_true,_false)

// string 
_string := 'i am a string'
print(_string)

// int 
_int := 2024
print(_int)

// float 
_float := 2.33333333333333
print(_float)


// table 
t := table('star','arg1','arg2')

table_set(t,'name','gin')

table_get(t,'name')

// table sugar

t[0] = 'assigned_name'
t['name'] = 'star'
t['ok'] =  def ok (){'i am ok '}

print(t)

t[0] = 666
t.name = 'new_star'

print(t)



// package export
t 

 
