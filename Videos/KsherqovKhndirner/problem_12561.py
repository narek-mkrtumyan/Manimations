import sys
sys.path.append('../../')
from Functions.qarakusi import *


class Problem12561(ScalesScene):
    def construct(self):
        
        first_shop = VGroup(BagOfMandarins(), BagOfMandarins()).arrange(buff=0.5)

        second_shop = VGroup(
            BagOfMandarins(),
            VGroup(BucketOfMandarins(), Tex('$10$ կգ', font_size=17
        ).shift([0, -0.15, 0]))).arrange(buff=0.5)

        third_shop = VGroup(
            BagOfMandarins(), VGroup(BucketOfMandarins(), Tex('$10$ կգ', font_size=17).move_to([0, -0.15, 0])),
            BagOfMandarins(), VGroup(BucketOfMandarins(), Tex('$10$ կգ', font_size=17).move_to([0, -0.15, 0])),
            BagOfMandarins(), VGroup(BucketOfMandarins(), Tex('$10$ կգ', font_size=17).move_to([0, -0.15, 0])),
            BagOfMandarins(), VGroup(BucketOfMandarins(), Tex('$10$ կգ', font_size=17).move_to([0, -0.15, 0]))
        ).arrange(buff=0.5)

        third_shop_buckets = VGroup(third_shop[1], third_shop[3], third_shop[5], third_shop[7]).shift(DOWN)
        third_shop_bags = VGroup(third_shop[0], third_shop[2], third_shop[4], third_shop[6]).shift(DOWN)

        VGroup(first_shop, second_shop, third_shop).arrange(DOWN, buff=0.75, aligned_edge=LEFT).shift([-1.5, 1, 0])

        large_bag_of_mndos =  BagOfMandarins('large').move_to(first_shop.get_center())

        rearranged_third_shop = VGroup(*third_shop_bags.copy(), *third_shop_buckets.copy()).arrange(buff=0.5)
        rearranged_third_shop.move_to(third_shop.get_center())

        big_bucket = VGroup(BucketOfMandarins().scale(1.5), Tex('$40$ կգ', font_size=25).move_to([0, -0.3, 0]))
        big_bucket.move_to(third_shop[4].get_center()).shift(0.25 * RIGHT)
        big_bucket.set_opacity(0)



# ANIMATIONS

        # self.add(first_shop, second_shop, third_shop, rearranged_third_shop)
        # self.wait()
        # self.wait()

        self.play(FadeIn(large_bag_of_mndos))
        self.wait()

        self.play(
            FadeOut(large_bag_of_mndos),
            FadeIn(first_shop)
        )
        self.wait()

        self.play(ReplacementTransform(first_shop[0].copy(), second_shop[0]))
        self.wait()

        self.play(FadeIn(second_shop[1]))
        self.wait()

        self.play(
            AnimationGroup(
                ReplacementTransform(second_shop.copy(), third_shop[0:2]),
                ReplacementTransform(second_shop.copy(), third_shop[2:4]),
                ReplacementTransform(second_shop.copy(), third_shop[4:6]),
                ReplacementTransform(second_shop.copy(), third_shop[6:8]),
                lag_ratio=0.75
            )
        )
        self.wait()

        self.play(third_shop_buckets.animate().shift(DOWN))

        self.play(
            ReplacementTransform(third_shop_bags, rearranged_third_shop[:4]),
            *[third_shop_buckets[i].animate.move_to(rearranged_third_shop[4 + i].get_center() - np.array([0, 1, 0])) for  i in range(4)]
        )

        self.play(ReplacementTransform(third_shop_buckets, rearranged_third_shop[4:]))
        self.wait()

        self.play(
            *[rearranged_third_shop[i].animate.move_to(big_bucket.get_center()).set_opacity(0) for  i in range(4, 8)],
            big_bucket.animate.set_opacity(1)
        )
        self.wait()
        # self.play(FadeOut(rearranged_third_shop[4:]))
        # self.play(FadeIn(big_bucket))


        # self.play(
        #     third_shop_bags[1:].animate.arrange(buff=0.5).next_to(third_shop_bags[0], RIGHT, buff=0.5),
        #     third_shop_buckets.animate.arrange(buff=0.5).move_to(buckets_center).shift(DOWN),
        # )







        
        # shop = FruitShop()
        # mndos = VGroup(*[Mandarins() for i in range(6)]).arrange(buff=0.06).move_to(shop.shelf.get_center()).shift(0.03 * RIGHT)
        # mandarin_shop = VGroup(shop, *mndos)

        # mandarin_shop_1 = mandarin_shop.copy().scale(0.5).shift([-4, 2.5, 0])
        # mandarin_shop_2 = mandarin_shop.copy()[:4].scale(0.5).shift([-4, 0, 0])

        # second_shop_extra_10_kg = Tex(r'+', r'$10$ կգ', font_size=60, tex_template=ARMTEX)
        # second_shop_extra_10_kg.next_to(mandarin_shop_2).shift(0.5 * DOWN)

        # second_shop_weight_10_kg = Weight(10, 5).move_to(second_shop_extra_10_kg[1].get_center())

        # self.add(mandarin_shop_1, mandarin_shop_2, second_shop_extra_10_kg)
        # self.play(ReplacementTransform(second_shop_extra_10_kg[1], second_shop_weight_10_kg))
        # self.wait()

        

class  test_test(Scene):
    def construct(self):
        self.add()

