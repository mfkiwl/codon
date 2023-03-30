import myext as m

def equal(v, a, b, tag):
    return v.a == a and v.b == b and v.tag == tag

# functions #
#############

assert m.f1(2.2, 3.3) == (2.2, 3.3)
assert m.f1(2.2, 3.3) == (2.2, 3.3)
assert m.f1(3.3) == (3.3, 2.22)
assert m.f1() == (1.11, 2.22)
assert m.f1(a=2.2, b=3.3) == (2.2, 3.3)
assert m.f1(2.2, b=3.3) == (2.2, 3.3)
assert m.f1(b=3.3, a=2.2) == (2.2, 3.3)
assert m.f1(a=2.2) == (2.2, 2.22)
assert m.f1(b=3.3) == (1.11, 3.3)

try:
    m.f1(1.1, 2.2, 3.3)
except:
    pass
else:
    assert False

try:
    m.f1(z=1)
except:
    pass
else:
    assert False

assert m.f2() == ({1: 'one'}, {2}, [3])

try:
    m.f2(1)
except:
    pass
else:
    assert False

try:
    m.f2(z=1, y=5)
except:
    pass
else:
    assert False

assert m.f3(42) == 84
assert m.f3(1.5) == 3.0
assert m.f3('x') == 'xx'

try:
    m.f3(1, 2)
except:
    pass
else:
    assert False

try:
    m.f3(a=1, b=2)
except:
    pass
else:
    assert False

assert m.f4() == ['f4()']
assert m.f4(2.2, 3.3) == (2.2, 3.3)
assert m.f4(3.3) == (3.3, 2.22)
assert m.f4(a=2.2, b=3.3) == (2.2, 3.3)
assert m.f4(2.2, b=3.3) == (2.2, 3.3)
assert m.f4(b=3.3, a=2.2) == (2.2, 3.3)
assert m.f4(a=2.2) == (2.2, 2.22)
assert m.f4(b=3.3) == (1.11, 3.3)
assert m.f4('foo') == ('foo', 'foo')
assert m.f4({1}) == {1}
assert m.f5() is None
assert equal(m.f6(1.9, 't'), 1.9, 1.9, 't')

# constructors #
################

x = m.Vec(3.14, 4.2, 'x')
y = m.Vec(100, 1000, tag='y')
z = m.Vec(b=2.2, a=1.1)
s = m.Vec(10)
t = m.Vec(b=11)
r = m.Vec(3, 4)

assert equal(x, 3.14, 4.2, 'x')
assert equal(y, 100, 1000, 'y')
assert equal(z, 1.1, 2.2, 'v0')
assert equal(s, 10, 0.0, 'v1')
assert equal(t, 0.0, 11, 'v2')

try:
    m.Vec(tag=10, a=1, b=2)
except:
    pass
else:
    assert False

# to-str #
##########

assert str(x) == 'x: <3.14, 4.2>'
assert repr(x) == "Vec(3.14, 4.2, 'x')"

# methods #
###########

assert x.foo(2.2, 3.3) == (3.14, 2.2, 3.3)
assert y.foo(3.3) == (100, 3.3, 2.22)
assert z.foo() == (1.1, 1.11, 2.22)
assert x.foo(a=2.2, b=3.3) == (3.14, 2.2, 3.3)
assert x.foo(2.2, b=3.3) == (3.14, 2.2, 3.3)
assert x.foo(b=3.3, a=2.2) == (3.14, 2.2, 3.3)
assert x.foo(a=2.2) == (3.14, 2.2, 2.22)
assert x.foo(b=3.3) == (3.14, 1.11, 3.3)

try:
    x.foo(1, a=1)
except:
    pass
else:
    assert False

try:
    x.foo(1, 2, b=2)
except:
    pass
else:
    assert False

try:
    x.foo(1, z=2)
except:
    pass
else:
    assert False

assert equal(x.bar(), 3.14, 4.2, 'x')
assert equal(y.bar(), 100, 1000, 'y')
assert equal(z.bar(), 1.1, 2.2, 'v0')
assert equal(s.bar(), 10, 0.0, 'v1')
assert equal(t.bar(), 0.0, 11, 'v2')

try:
    x.bar(1)
except:
    pass
else:
    assert False

try:
    x.bar(z=1)
except:
    pass
else:
    assert False

assert m.Vec.baz(2.2, 3.3) == (2.2, 3.3)
assert x.baz(2.2, 3.3) == (2.2, 3.3)
assert m.Vec.baz(3.3) == (3.3, 2.22)
assert m.Vec.baz() == (1.11, 2.22)
assert m.Vec.baz(a=2.2, b=3.3) == (2.2, 3.3)
assert m.Vec.baz(2.2, b=3.3) == (2.2, 3.3)
assert m.Vec.baz(b=3.3, a=2.2) == (2.2, 3.3)
assert m.Vec.baz(a=2.2) == (2.2, 2.22)
assert m.Vec.baz(b=3.3) == (1.11, 3.3)

try:
    m.Vec.baz(1, a=1)
except:
    pass
else:
    assert False

try:
    m.Vec.baz(1, 2, b=2)
except:
    pass
else:
    assert False

assert m.Vec.nop() == 'nop'
assert x.nop() == 'nop'
assert y.c == 1100

# fields #
##########

t.a = 99
assert equal(t, 99, 11, 'v2')
t.tag = 't'
assert equal(t, 99, 11, 't')

# magics #
##########

assert equal(+y, 100, 1000, '(+y)')
assert equal(-y, -100, -1000, '(-y)')
assert equal(~y, -101, -1001, '(~y)')
assert abs(r) == 5.0
assert bool(y)
assert not bool(m.Vec())
assert len(x) == 1
assert len(x + y) == 5
assert hash(y) == 1100

assert equal(x + y, 103.14, 1004.2, '(x+y)')
try:
    x + 'x'
except:
    pass
else:
    assert False
assert equal(x + y + y, 203.14, 2004.2, '((x+y)+y)')
assert equal(y + 50.5, 150.5, 1050.5, '(y+50.5)')
assert equal(y + 50, 150, 1050, '(y++50)')
# assert equal(50.5 + y, 150.5, 1050.5, '(y+50.5)')  # support for r-magics?
assert equal(y - x, 96.86, 995.8, '(y-x)')
assert equal(y * 3.5, 350.0, 3500.0, '(y*3.5)')
assert equal(y // 3, 33, 333, '(y//3)')
assert equal(y / 2.5, 40.0, 400.0, '(y/2.5)')
try:
    divmod(y, 1)
except ArithmeticError as e:
    assert str(e) == 'no divmod'
else:
    assert False
assert equal(y % 7, 2, 6, '(y%7)')
assert equal(y ** 2, 10000, 1000000, '(y**2)')
assert equal(y << 1, 200, 2000, '(y<<1)')
assert equal(y >> 2, 25, 250, '(y>>2)')
assert equal(y & 77, 68, 72, '(y&77)')
assert equal(y | 77, 109, 1005, '(y|77)')
assert equal(y ^ 77, 41, 933, '(y^77)')
assert y @ r == 4300

def dup(v):
    return m.Vec(v.a, v.b, v.tag + '1')

y1 = dup(y)
y1 += x
assert equal(y1, 103.14, 1004.2, '(y1+=x)')

y1 = dup(y)
y1 += 1.5
assert equal(y1, 101.5, 1001.5, '(y1+=1.5)')

y1 = dup(y)
y1 -= x
assert equal(y1, 96.86, 995.8, '(y1-=x)')

y1 = dup(y)
y1 *= 3.5
assert equal(y1, 350.0, 3500.0, '(y1*=3.5)')

y1 = dup(y)
y1 //= 3
assert equal(y1, 33, 333, '(y1//=3)')

y1 = dup(y)
y1 /= 2.5
assert equal(y1, 40.0, 400.0, '(y1/=2.5)')

y1 = dup(y)
y1 %= 7
assert equal(y1, 2, 6, '(y1%=7)')

y1 = dup(y)
y1 **= 2
assert equal(y1, 10000, 1000000, '(y1**=2)')

y1 = dup(y)
y1 <<= 1
assert equal(y1, 200, 2000, '(y1<<=1)')

y1 = dup(y)
y1 >>= 2
assert equal(y1, 25, 250, '(y1>>=2)')

y1 = dup(y)
y1 &= 77
assert equal(y1, 68, 72, '(y1&=77)')

y1 = dup(y)
y1 |= 77
assert equal(y1, 109, 1005, '(y1|=77)')

y1 = dup(y)
y1 ^= 77
assert equal(y1, 41, 933, '(y1^=77)')

y1 = dup(y)
y1 @= 3.5
assert equal(y1, 350.0, 3500.0, '(y1@=3.5)')

assert equal(y(), 100, 1000, '(y())')
assert x(2.2, 3.3) == (3.14, 2.2, 3.3)
assert y(3.3) == (100, 3.3, 2.22)
assert x(a=2.2, b=3.3) == (3.14, 2.2, 3.3)
assert x(2.2, b=3.3) == (3.14, 2.2, 3.3)
assert x(b=3.3, a=2.2) == (3.14, 2.2, 3.3)
assert x(a=2.2) == (3.14, 2.2, 2.22)
assert x(b=3.3) == (3.14, 1.11, 3.3)
assert y('foo') == (100.0, 1000.0, 'foo')

assert x == x
assert x != y
assert r == m.Vec(3, 4, '?')
assert x < y
assert y > x
assert x <= y
assert y >= x
assert y <= y
assert x >= x

assert list(iter(x)) == ['x']
assert list(iter(x+y+y)) == list('((x+y)+y)')

assert 100 in y
assert 1000 in y
assert 100.5 not in y
assert 'y' in y
assert 'x' not in y

assert y[0] == 100
assert y[1] == 1000
assert y[11] == 1100
try:
    y[-1]
except KeyError as e:
    assert str(e) == "'bad vec key -1'"
else:
    assert False

y[0] = 99.9
assert equal(y, 99.9, 1000, 'y')
y[1] = -42.6
assert equal(y, 99.9, -42.6, 'y')
y[11] = 7.7
assert equal(y, 7.7, 7.7, 'y')
try:
    y[2] = 1.2
except KeyError as e:
    assert str(e) == "'bad vec key 2 with val 1.2'"
else:
    assert False
del y[1]
assert equal(y, 7.7, 0.0, 'y')
