## OPERATOR PRECEDENCE (in order highest to lowest)
| Operator | Description |
|----------|-------------|
| (expressions...), [expressions...], {key: value...}, {expressions...} | Binding or parenthesized expression, list display, dictionary display, set display |
| x[index], x[index:index], x(arguments...), x.attribute | Subscription, slicing, call, attribute reference |
| await x | Await expression |
| ** | Exponentiation |
| +x, -x, ~x | Positive, negative, bitwise NOT |
| *, @, /, //, % | Multiplication, matrix multiplication, division, floor division, remainder 5 |
| +, - | Addition and subtraction |
| <<, >> | Shifts |
| & | Bitwise AND |
| ^ | Bitwise XOR |
| &#124; | Bitwise OR |
| in, not in, is, is not, <, <=, >, >=, !=, == | Comparisons, including membership tests and identity tests |
| not x | Boolean NOT |
| and | Boolean AND |
| or | Boolean OR |
| if – else | Conditional expression |
| lambda | Lambda expression |
| := | Assignment expression |
