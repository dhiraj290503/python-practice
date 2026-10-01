"""sets"""
## 1.Mutable
## 2.duplicates not allowed
## 3.unordered
## 4.semi-heterogenous

s={"a","b","c","d"}
s1={1,2,3,4}

print(s)
print(s1)

"""sets Methond"""
## 1. add()
## 2. update()
## 4. discard()
## 5. pop()
## 6. clear()

"""Set Mathematical Operations"""
## 7. union()
## 8. intersection()
## 9. difference()
## 10. symmetric_difference()

"""Set Comparison Methods"""
## 11. issubset()
## 12. issuperset()
## 13. isdisjoint()

##############################################################################

## add()                  → 1 element add
## update()               → multiple elements add
#
## remove()               → remove, error if absent
## discard()              → remove, no error if absent
## pop()                  → remove arbitrary element
## clear()                → remove everything
#
## union()                → ALL
## intersection()         → COMMON
## difference()           → FIRST ONLY
## symmetric_difference() → NON-COMMON
#
## issubset()             → A inside B?
## issuperset()           → B inside A?
## isdisjoint()           → NO COMMON?