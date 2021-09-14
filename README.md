**A PointSorter Class**
This class can sort a sequence of equally-sized float vectors in non-
decreasing order. The column order by which it sorts the points is from
index 0 to `l -1`, `l` the length of each vector. This ordering is identical
to how alphabetical strings are sorted.

In addition to performing sorting, this class
can also update the point mean and variance after each change to elements (i.e. inserting or deleting set C from the class).

**Instructions**

PointSorter can be used in more than one way.

In the first approach, data is loaded into the `PointSorter` at instantiation.

```
S = <s1,s2,s3>

q = PointSorter(S)

q.sort_it()

print("SORTED DATA")
print(q.newData)
```

In the second approach, data is inserted or deleted from `PointSorter` *without*
updating the mean or variance.

```
ADD = <s1,s2,s3,s4,s5>
DEL = <s3,s5>

q = PointSorter(np.empty(0,len(s1)))

for p in ADD: q.insert_point(p)
for p in DEL: q.delete_point(p)
```

In the last approach, data is inserted or
deleted from `PointSorter`, and
`PointSorter` updates the mean and variance
and referential extremum points
(if given a reference point).

```
ADD = <s1,s2,s3,s4,s5>
DEL = <s3,s5>

q = PointSorter(np.empty(0,len(s1)))

for a in ADD: q.log_delta_cache(ADD,1)
for d in DEL: q.log_delta_cache(DEL,-1)

# CALL q.update_extremum HERE if have reference point
q.update_points_from_cache(referencePoint = None)

print("POINT MEAN")
print(q.pointMean)
print("POINT VARIANCE")
print(q.pointVariance)

```
