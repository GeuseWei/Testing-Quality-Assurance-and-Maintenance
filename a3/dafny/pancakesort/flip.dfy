// flips (i.e., reverses) array elements in the range [0..num]
method flip (a: array<int>, num: int)
  requires a.Length > 0;
  requires 0 <= num < a.Length;
  ensures multiset(old(a[..])) == multiset(a[..]);
  ensures forall j :: 0 <= j <= num ==> a[j] == old(a[num-j]);
  ensures forall j :: num < j < a.Length ==> a[j] == old(a[j]);
  modifies a;
{
  var tmp:int;

  var i := 0;
  var j := num;
  while (i < j)
    decreases j-i;
    invariant i+j == num;
    invariant multiset(old(a[..])) == multiset(a[..]);
    invariant forall k :: num < k < a.Length ==>a[k] == old(a[k]);
    invariant forall k :: 0 <= k < i ==> a[k] == old(a[num - k]);
    invariant forall k :: i <= k <= j ==> a[k] == old(a[k]);
    invariant forall k:: j < k <= num ==> a[k] == old(a[num-k]);
  {
    tmp := a[i];
    a[i] := a[j];
    a[j] := tmp;
    i := i + 1;
    j := j - 1;
  }
}
