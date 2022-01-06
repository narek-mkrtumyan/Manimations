# FUNCTIONS USEFUL IN GEOMETRY
Also includes `armtex` package as `armenian_tex_template`.

## DONE

- Functions that only return something
    - LabelPoint(point, label, position)
        - returns label_A - MathTex('A')
    - DistanceBetweenCoordinates(a, b)
        - returns distance between coordinates a=[a_x, a_y, a_z] and b=[b_x, b_y, b_z]
    - DistanceBetweenPoints(A, B)
        - returns distance between points Dot_A, Dot_B
    - SegmentLength(AB)
        - returns distance between points Dot_A, Dot_B
    - SegmentEqualitySign1(AB)
        - returns 1 small line in the middle of segment AB
    - SegmentEqualitySign2(AB)
        - returns 2 small lines in the middle of segment AB
    - SegmentEqualitySign3(AB)
        - returns 3 small lines in the middle of segment AB
    - FilledAngle(line_1, line_3)
        - returns angle sign filled with some color
    - Angle2(line_1, line_2)
        - returns VGroup of 2 circular arcs representing an angle of two lines
    - Angle3(line_1, line_2)
        - returns VGroup of 3 circular arcs representing an angle of two lines
    - MathtexSegmentsEquality(labels)
        - returns MathTex('AB=CD')
    - MathtexCommonSegment(labels) labels=('A', 'B')
        - returns VGroup from 3 mobjects ('A''B' '-ն ընդհանուր է') # 'AB is common'
    - MathTexTrianglesEquality(abc, xyz)
        - MathTex('ABC=XYZ')
    - ConcludeFromStatementSystem(statements, conclusion)
        - returns VGroup of (statements, brace, => conclusion) - { statements => conclusion

    - TransformSegmentLabelsIntoStatement
        - returns list of 2 or 3 animations for Transforming segment into a statement 'A''B'
    - TransformSegmentsLabelsIntoEquality
        - returns list of 5 or 7 animations for Transforming segments into equality AB=BC
    - returns list of 3 or 4 animations for Transforming segment into a statement 'AB' and Writing '-ն ընդհանուր է' ('A''B''-is common')



- Functions that play some animations and return something
    - CircleFromSpinningRadius()
        - draws a circle with compass drawing tool (կարկին) effect
        - returns the circle


- Functions that only play some animations
    - 



## NEEDS TO BE DONE

- TriangleCongruence functions
    - SSS() needs to be deleted
    - PlaySSSWiggling() needs to be deleted
    - PlaySSSThickening() needs to be updated (like wiggling) or deleted
    - SSA()
    - PlaySSAWiggling()
    - PlaySSAThickening()
    - SAA()
    - PlaySAAWiggling()
    - PlaySAAThickening()

