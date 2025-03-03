## String methods 
|method|input|function|output|
|---|---|---|---|
|number of characters|`a = "I love coding!"`|`b = len(a)`|`b: 14`|
|array to string|`a = ["cat","dog","horse"]`|`b = ",".join(a)`|`b: "cat,dog,horse"`|
|string to array|`a = "cat,dog,horse"`|`b = a.split(",")`|`b: ["cat","dog","horse"]`|
|remove whitespace|`a = " cat "`|`b = a.strip()`|`b: "cat"`|
## Array methods
|method|input|function|output|
|---|---|---|---|
|insert last|`a = ["cat","dog"]`|`a.append("horse")`|`a: ["cat","dog","horse"]`|
|insert arbitrary|`a = ["cat","dog"]`|`a.insert(1, "horse")`|`a: ["cat","horse","dog"]`|
|remove and return last|`a = ["cat","dog"]`|`b = a.pop()`|`a: ["cat"] b: "dog"`|
|remove and return arbitrary|`a = ["cat","dog"]`|`b = a.pop(0)`|`a: ["dog"] b: "cat"`|
|empty list|`a = ["cat","dog"]`|`a.clear()`|`a: []`|

