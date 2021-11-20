# FUNCTIONS USEFUL IN GEOMETRY
Also includes `armtex` package as `armenian_tex_template`.

## DONE

- LabelPoint(point, label, position)
    - returns label_A - MathTex('A')
- DistanceBetweenCoordinates(a, b)
    - returns distance between coordinates a=[a_x, a_y, a_z] and b=[b_x, b_y, b_z]
- DistanceBetweenPoints(A, B)
    - returns distance between points Dot_A, Dot_B
- SegmentLength(AB)
    - returns distance between points Dot_A, Dot_B
- SegmentEqualitySign_1(AB)
    - returns a small line in the middle of segment AB
- SegmentEqualitySign_2(AB)
    - returns 2 small lines in the middle of segment AB
- MathtexSegmentsEquality(labels)
    - returns MathTex('AB=CD')
- MathtexCommonSegment(labels) labels=('A', 'B')
    - returns Mathtex('AB-ն ընդհանուր է') # AB is common
- ConcludeFromStatementSystem(statements, conclusion)
    - returns Group of statements, brace and conclusion - { statements => conclusion
- MathTexTrianglesEquality(abc, xyz)
    - MathTex('ABC=XYZ)

- CircleFunctions

    - CircleFromSpinningRadius()
        - draws a circle with compass drawing tool (կարկին) effect
        - returns the circle

## NEEDS TO BE DONE

