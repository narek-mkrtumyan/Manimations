import sys
sys.path.append("../../../")
from Functions.QarakusiFunctions import *

class prob_12546(Scene):
	def construct(self):
		#draw the first segment and write 'Ռուբեն' to the left of the segment
		#copy that segment, shift down, expand by some length (orange), and write 'Լիլիթ' to the left of it

			segment_0 = Segment([-3, 2.5, 0], [-2, 2.5, 0])
			txt_0 = MathTex(r'\textrm{Ռուբեն}', tex_template=armenian_tex_template,
         		font_size=40).next_to(segment_0[0][0], 4 * LEFT)


			segment_ten = Segment([-2, 2.5, 0], [0, 2.5,0], color=ORANGE).shift(1.5 * DOWN)
			txt_or = MathTex(r'10', font_size=40).next_to(segment_ten.get_center(),UP)

			segment_or = VGroup(segment_ten,txt_or)

			segment_1 = VGroup(segment_0.copy(),segment_or)
			txt_1 = MathTex(r'\textrm{Լիլիթ}', tex_template=armenian_tex_template,
				font_size=40).next_to(segment_1[0][0], 4 * LEFT).shift(1.5 * DOWN)

			self.play(Create(segment_0))
			self.wait()

			self.play(Write(txt_0))
			self.wait()

			self.play(segment_1[0].animate.shift(1.5*DOWN))
			self.wait()

			self.play(Create(segment_1[1]))
			self.wait()
			
			self.play(
				Write(txt_1),
				#Write(txt_or)
			)
			self.wait()

		#brace that segments from the right, and write 24
			segments = VGroup(segment_0,segment_1)
			br = Brace(segments, RIGHT).shift(RIGHT)
			txt_br = br.get_text("24")

			self.play(Write(br))
			self.wait()

			self.play(Write(txt_br))
			self.wait()

		#using Scissors().cut_in(self) and Scissors().cut_out(self) 
		#cut the extra part of the second line and move it a little bit to the right
			p_cut = segment_or[0][1].get_center()
			scissors = Scissors(p_cut)

			scissors.cut(self)
			self.play(VGroup(segment_1[1]).animate(run_time=1.0, rate_func=smooth).shift(0.5 * RIGHT))
			scissors.fade_out(self)
			self.wait()

		#copy and bring 24 and 10 to the bottom and transform into 24-10 = 14
			txt_exp_1 = MathTex(
					'24',
					'-',
					'10',
					'=',
					'14',
					font_size=40
				).shift(DOWN)

			self.play(ReplacementTransform(txt_br.copy(),txt_exp_1[0]))
			self.wait()

			self.play(ReplacementTransform(txt_or.copy(),txt_exp_1[2]))
			self.wait()
			for i in [1,3,4]:
				self.play(Write(txt_exp_1[i]))
			self.wait()

		#indicate first segment and than the second segment, than write 14/2 = 7
			txt_exp_2 = MathTex(
					'14 : 2 =',
					'7',
					font_size=40
				).shift(2*DOWN)

			self.play(Indicate(segment_0))
			self.wait()

			self.play(Indicate(segment_1[0]))
			self.wait()

			self.play(Write(txt_exp_2))
			self.wait()

		#copy and move that 7 and place on top of each segment
			txt_seg_0 = MathTex(r'7', font_size=40).next_to(segment_0.get_center(), UP)
			txt_seg_1 = txt_seg_0.copy().next_to(segment_1[0].get_center(), UP)

			txt_seg = VGroup(txt_seg_0,txt_seg_1)

			self.play(ReplacementTransform(txt_exp_2[1].copy(),txt_seg))
			self.wait()
		
		#take the 7 of the first segment in the green rectangle
			box = SurroundingRectangle(txt_seg_0, color=GREEN)

			self.play(Create(box))
			self.wait()
