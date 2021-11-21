# SCENE PerpBisect
C-ն հավասարահեռ է A և B կետերից, <=> C-ն գտնվում է AB-ի միջնուղղահայացի վրա
## DONE
- Մաս 1 (AC=BC => C-ն միջնուղղահայացի վրա է)
    - Գծագիր
        - Վերցնել որևէ A և B կետեր, որոնք լինելու են հատվածի ծայրակետերը և ցանկացած C կետ, որը միացնել A և B կետերին
        - Քանի որ AC < BC, ուստի AC ներկել կարմիր, իսկ BC-ն կանաչ
        - C-ն տեղաշարժել ու մոտեցնել AB-ի միջնուղղահայացին, որին զուգահեռ երկու հատվածների գույները մոտենում են նարնջագույնին
        - Երբ հատվածները դառնում են իրար հավասար հատվածները սարքել մեր ստանդարտ նարնջագույնը
        - AC և BC հատվածների վրա դնել հավասար հատվածների նշանները
        - Կառուցել AB հատվածը և նշել AB հատվածի M միջնակետը՝ նշելով որ AM=MC
        - Տանել բարակ MC բաց կանաչ ուղիղը
        - ACM եռանկյունը ներկել դեղին, իսկ BMC եռանկյունը ներկել բաց կանաչ
        - Էկրանը տեղափոխել աջ, լուծման համար տեղ բացվի
    - Լուծում
        - Հերթով հաստացնել ու բարակացնելով եռանկյունների համապատասխան կողմերը և աջի վրա գրել հավասարությունները
        - եռանկյունների կողմերի հավասարություններից եզրակացնել, որ եռանկյունները հավասար են և գծագրի վրա նշել, որ \angle AMC = \angle BMC = 90^o:
        - C կետը տանել վերև-ներքև ու միշտ AC և BC վրա նշել իրար հավասար։


- Մաս 2 (միջնուղղահայացի վրա է => AC=BC)
    - 

### Functions
- Uses some functions from GeometryFunctions.py
    - more about that functions in Functions for Geometry folder
- Create_ABC_MoveC_To_PB
    - Creates A B C points
    - Creates CA and CB segments
    - Calls move_C_to_PB_and_change_colors()
- move_C_to_PB_and_change_colors
    - Moves point C to the PB (perpendicular bisector) of AB
    - Simultaneously changes colors of CA an CB from RED and GREEN to ORANGE
- Add_M_MC
    - Puts the equality signs on CA and CB
    - Creates AB, M
    - Puts equality signs on AM and BM
    - Creates MC
    - Colors ACM and BCM
    - Shifts camera to right
- move_C_down_and_up
    - Moves point C along PB down and up

see more about each functions in it's docstrings

### Animations
- 

## NEEDS TO BE DONE

### Functions
- 

### Animations


Այս ամբողջը մասշտաբով փոքրացնել ու տեղավորել էկրանի ձախ 1/3 մասում։

Էկրանի աջ կեսում գծել AB հատվածը, նշել M միջնակետը ու տանել միջնուղղահայացը՝ նշելով AM=MB և \angle AMC = \angle BMC։ Միջնուղղահայացի վրա նշել C կետ, միացնել A և B կետերին։
AMC եռանկյունը ներկել դեղին, իսկ BMC-ն կանաչ։ Գծագրի վրա խոշորացնելով նշել, իսկ աջ մասում գրելով  պայմանները, եռանկյունների հավասարության առաջին հայտանիշով եզրակացնել, որ եռանկյունները հավասար են, հետևաբար AC=MC։

Այս երկրորդ կտորի գծագիրն ու տեքստը փոքրացնելով բերել էկրանի աջ կես, իսկ ձախ 1/3 մասում գծածը մեծացնել ու տեղավորել էկրանի ձախ կեսում։


Ներքևում գրել, "Եթե հավասարահեռ է երկու կետերից, ուրեմն միջնուղղահայացի վրա է"
Տակը գրել   " Եթե հատվածի միջնուղղահայացի վրա է, ուրեմն հավասարահեռ է ծայրակետերից"։

