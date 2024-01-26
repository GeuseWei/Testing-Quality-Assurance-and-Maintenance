/*

   The method CalcTerm (m, n) computes 5*m-3*n using only arithmetic
   operations +5, -1, and -3.

   Fix the 'invariant' and 'decreases' annotations such that it verifies

*/
function abs(m: int): nat
{ if m>0 then m else -m }

method CalcTerm(m: int, n: nat) returns (res: int)
  ensures res == 5*m-3*n;
{
  var m1: nat := abs(m);
  var n1: nat := n;
  res := 0;

  while (m1!=0)
    invariant res == 5*(abs(m) - m1)
    decreases m1
  {
    res := res+5;
    m1 := m1-1;
  }

  if (m<0) { res := -res; }
  var old_res := res;

  while (n1!=0)
    invariant res == old_res - 3*(n-n1);
    decreases n1;
  {
    res := res-3;
    n1 := n1-1;
  }
}
