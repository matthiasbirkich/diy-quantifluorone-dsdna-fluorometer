# RC2 prediction-interval display fix

RC1 could show LOD/LOQ after a multipoint sample measurement instead of the
individual prediction interval.

RC2 uses this display logic:

```text
Before sample:
LOD ... LOQ ...

After multipoint sample:
95% PI +/- ...

If interval statistics are unavailable:
95% PI unavailable
```

LOD and LOQ remain available under:

```text
SELECT → CAL STATUS
```

For the minimal update, replace:

```text
code.py
quantifluorone_app.py
```

Copying the complete RC2 package is also supported.
