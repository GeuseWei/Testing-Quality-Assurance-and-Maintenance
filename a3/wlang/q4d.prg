havoc x, y;
assume y >= 0;
c := 0;
r := 0;
while c < y
inv c <= y and r = x * c
do
{
  r := r + x;
  c := c + 1
};

assert r = x * y