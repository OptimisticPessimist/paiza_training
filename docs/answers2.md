#### 解答例

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"`を以下の形に変形させよ
1. 'ABCABCABC'
```python
>>> s[0:3] * 3
```

1. 'DGJMPSV'
```python
>>> s[3:-3:3]
```

1. 'XSNI'
```python
>>> s[-3:4:-5]
```