# %GC in sliding window calculation

Sliding window program to compute the %GC in sequence of nucleotides.

## Input

- Mode (file or sequence input)
- DNA sequence
- The window size (assume the window increment is 1)

```python
py %gc_sliding_window.py 1 NCNACT 3
```

### output

- Nucleotide number
- %GC for each window

```Terminal
Start processing ...

Window 1: NCN
Nucleotide number: 3
There are 0.0 Gs, 1.0 Cs, 0.0 As and 0.0 Ts, in the DNA strand.
GC content is: 33.333333333333336%
======================
Window 2: CNA
Nucleotide number: 3
There are 0.0 Gs, 1.0 Cs, 1.0 As and 0.0 Ts, in the DNA strand.
GC content is: 33.333333333333336%
======================
Window 3: NAC
Nucleotide number: 3
There are 0.0 Gs, 1.0 Cs, 1.0 As and 0.0 Ts, in the DNA strand.
GC content is: 33.333333333333336%
======================
Window 4: ACT
Nucleotide number: 3
There are 0.0 Gs, 1.0 Cs, 1.0 As and 1.0 Ts, in the DNA strand.
GC content is: 33.333333333333336%
======================

End processing ...
```

## Resources

<https://www.geeksforgeeks.org/window-sliding-technique/>
<https://en.wikipedia.org/wiki/GC-content#:~:text=In%20molecular%20biology%20and%20genetics,)%20or%20cytosine%20(C).>
