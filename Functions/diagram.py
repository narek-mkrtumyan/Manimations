from .maserovkhndirscene import *




### Մասերով խնդրի մասերը
class Diagram(VGroup):
    def __init__(
        self,
        parts: list[list],
        names: list[MathTex or DecimalNumber],
        brace: bool = False,
        total: MathTex or DecimalNumber = MathTex(r'.', font_size=1),
        **kwargs
    ):
        VGroup.__init__(self)
        assert len(parts) == len(names), "Length of 'parts' must match length of 'names'"

        players_number = len(parts)
        self.player = parts.copy()
        self.player_name = names.copy()
        self.list = parts
        for i in range(players_number):
            self.player[i] = [0 for _ in parts[i]]
            pointer = 0
            for j in range(len(parts[i])):

                if parts[i][j][0] % 100 == 0:
                    self.player[i][j] = Segment(
                            start=[pointer, players_number/2 - i, 0],
                            end= [pointer + parts[i][j][0]/1000, players_number/2 - i, 0],
                            text= parts[i][j][1]
                        )
                elif parts[i][j][0] % 2 == 0:
                    self.player[i][j] = Segment(
                            start=[pointer, players_number/2 - i, 0],
                            end= [pointer + parts[i][j][0]/1000, players_number/2 - i, 0],
                            text= parts[i][j][1], color = ORANGE
                        )
                else:
                    self.player[i][j] = Segment(
                            start=[pointer, players_number/2 - i, 0],
                            end= [pointer + parts[i][j][0]/1000, players_number/2 - i, 0],
                            text= parts[i][j][1], color = GREEN
                        )

                pointer += parts[i][j][0]/1000
                self.add(self.player[i][j])
            self.player_name[i].move_to([-1, players_number/2 - i, 0], aligned_edge=RIGHT)
            self.add(self.player_name[i])
            self.scale_ratio = 1

        #self.brace = brace
        if brace:
            self.brace = Brace(VGroup(*[ VGroup(*self.player[i]) for i in range(players_number)]),  RIGHT, buff=0.5)
            self.total = total.next_to(self.brace, RIGHT, buff=0.5)
            self.add(self.brace, self.total)
        else:
            self.brace = brace


    def set_total(
        self,
        new_total: MathTex or DecimalNumber,
        scene: bool or Scene = False
    ):
        assert self.brace, "There is no brace "
        self.remove(self.total)
        new_total.next_to(self.brace, RIGHT, buff=0.5)
        
        self.add(self.total)
        if scene:
            scene.play(ReplacementTransform(self.total, new_total.copy()))
        self.total = new_total


    def create_by_copying(
        self,
        scene: Scene,
        coping_list: list[list]
    ):
        assert len(coping_list) == len(self.player), "Length of 'coping_list' must match length of 'self.player'"
        scene.play(AnimationGroup(*[Write(i) for i in self.player_name], lag_ratio=0.5))
        for i in range(len(self.player)):
            assert len(coping_list[i]) == len(self.player[i]), f"Length of 'coping_list[{i}]' must match length of 'self.player[{i}]'"
            for j in range(len(self.player[i])):
                if coping_list[i][j] == 0:
                    scene.play(Create(self.player[i][j]))

                elif coping_list[i][j] != -1:
                    verifying = True
                    for k in range(i):
                        for l in range(len(self.player[k])):
                            if coping_list[i][j] == coping_list[k][l]:
                                scene.play(ReplacementTransform(self.player[k][l].copy(), self.player[i][j]))
                                verifying = False
                                break
                        if not verifying:
                            break

                    if verifying:
                        scene.play(Create(self.player[i][j]))

                scene.wait()
    

    def create_by_order_and_steps(
        self,
        scene: Scene,
        order: list[int],
        steps: list[list[int]]
    ):
        #
        # Segments must be numbered for each "player"
        # Segments with numbers 0 will not be copied and the rest will be according to matching numbers
        #
        assert len(order) == len(self.player) and len(steps) == len(self.player), "Length of 'order' and 'steps' must match length of 'self.player'"

        interation_number = max([len(i) for i in steps])

        scene.play(AnimationGroup(*[Write(self.player_name[i]) for i in order], lag_ratio=0.5))

        for i in range(interation_number):
            for j in order:
                if i < len(steps[j]):
                    if i == 0:
                        ran = range(steps[j][i])
                    else:
                        ran = range(steps[j][i-1], steps[j][i])
                    for k in ran:
                        scene.play(Create(self.player[j][k]))
                    scene.wait()

    def crate_brace(
        self,
        scene: Scene
    ):
        if self.brace:
            scene.play(Write(self.brace))
            scene.play(Write(self.total))
    

    def animate_superscale(
        self,
        scene: Scene,
        scale_ratio: float,
        move_to_point: list[float] = [0, 0, 0]
    ):
        self.generate_target()
        self.target.scale(scale_ratio)
        for name in self.target.player_name:
            name.shift((scale_ratio -1) * RIGHT).scale(1/scale_ratio)
        for player in self.target.player:
            for segment in player:
                if segment.text:
                    segment.text.scale(1/scale_ratio).next_to(segment.line.get_center(), segment.position)
                segment.endmark_left.scale(1/scale_ratio)  
                segment.endmark_right.scale(1/scale_ratio)
        self.target.move_to(move_to_point)
        scene.play(MoveToTarget(self))
        self.scale_ratio *= scale_ratio


    def show_equal_parts(
        self,
        scene: Scene,
        equal_list: list[int]
    ):
        assert len(equal_list) == len(self.player), "Length of 'equal_parts' must match length of 'self.player'"
        for i in range(len(self.player)):
            assert len(equal_list[i]) == len(self.player[i]), f"Length of 'equal_parts[{i}]' must match length of 'self.player[{i}]'"
            for j in range(len(self.player[i])):
                if equal_list[i][j] != 0:
                    verifying = True
                    for k in range(i+1):
                        for l in range(len(self.player[k])):
                            if equal_list[i][j] == equal_list[k][l]:
                                if i != k:
                                    scene.play(ReplacementTransform(self.player[k][l].copy().set_color(YELLOW), self.player[i][j]))
                                    verifying = False
                                    break
                                else:
                                    segment_copy = self.player[k][l].copy().set_color(YELLOW)
                                    
                                    scene.play(
                                        segment_copy.animate.next_to(VGroup(segment_copy, self.player[i][j]), UP),
                                        run_time = 0.5, rate_func = rush_into
                                    )
                                    scene.play(
                                        ReplacementTransform(segment_copy, self.player[i][j]), 
                                        run_time = 0.5, rate_func = rush_from
                                    )
                                    verifying = False
                                    break

                        if not verifying:
                            break

    def segment_perpendicular_projection(
        self,
        scene: Scene,
        project_from: list[int],
        project_to: int,
        add: bool = False,
        subtract: bool = False,
        replace: bool = False,
        apply_to: list or bool = False
    ):
        p_left = [0, 0, 0]
        p_left[0] = self.player[project_from[0]][project_from[1]].endmark_left.get_center()[0]
        p_left[1] = self.player[project_to][0].endmark_left.get_center()[1]
        d_left = DashedLine(self.player[project_from[0]][project_from[1]].endmark_left.get_center(), p_left)


        p_right = [0, 0, 0]
        p_right[0] = self.player[project_from[0]][project_from[1]].endmark_right.get_center()[0]
        p_right[1] = self.player[project_to][0].endmark_right.get_center()[1]
        d_right = DashedLine(self.player[project_from[0]][project_from[1]].endmark_right.get_center(), p_right)
        new_line = Line(p_left, p_right, color=self.player[project_from[0]][project_from[1]].line.get_color())
        
        
        self.generate_target()
        if apply_to:
            for i in apply_to:
                if i != project_from[0] and i != project_to:
                    self.target.player_name[i].set_opacity(0.5)
                    for s in self.target.player[i]:
                        s.set_opacity(0.5)
        else:
            self.target.set_opacity(0.5)
        #self.target.player[project_from[0]][project_from[1]].set_opacity(1)
        scene.play(MoveToTarget(self))
        scene.play(Create(d_left), Create(d_right), FadeIn(new_line, run_time = 1.5))
        scene.wait(2)
        if replace:
            verifying = False
            to_remove = VGroup()
            cut_segment_start_number: int
            for i in range(len(self.player[project_to])):
                #if abs(p_left - segment.endmark_left.get_center()[0]) < 0.1:
                segment = self.player[project_to][i]

                if verifying:
                    to_remove.add(segment)
                    self.remove(segment)
                    #self.player[project_to].pop(i)
               
                if segment.endmark_right.get_center()[0] > p_left[0] - 0.1 and not verifying:
                   
                    to_remove.add(segment)
                    ##TODO
                    self.remove(segment)
                    cut_segment_start_number = i
                    
                    if abs(p_left[0] - segment.endmark_right.get_center()[0]) < 0.1:
                        color = segment.line.get_color()
                        text = segment.text
                    else:
                        color = GREEN
                        text = False
                        #color=self.player[project_from[0]][project_from[1]].line.get_color()
                    if i != 0:    
                        left_segment = Segment(segment.endmark_left.get_center(), p_left, color=color, text=text)
                        self.player[project_to][i] = left_segment
                        self.add(self.player[project_to][i])
                    
                    

                    if i == len(self.player[project_to])-1:
                        if i != 0:
                            new_segment = Segment(p_left, p_right, color=self.player[project_from[0]][project_from[1]].line.get_color())
                            self.player[project_to].append(new_segment) 
                            self.add(self.player[project_to][i+1])
                            if segment.endmark_right.get_center()[0] > p_right[0] + 0.1:
                                right_segment = Segment(p_right, segment.endmark_left.get_center(), color=GREEN)
                                self.player[project_to].append(right_segment)
                                self.add(self.player[project_to][i+2])
                        else:
                            new_segment = Segment(p_left, p_right, color=self.player[project_from[0]][project_from[1]].line.get_color())
                            #to_remove.add(self.player[project_to][i])
                            self.remove()
                            scene.remove(self.player[project_to][i])

                            self.player[project_to][i] = new_segment 
                            self.add(self.player[project_to][i])
                            if segment.endmark_right.get_center()[0] > p_right[0] + 0.1:
                                right_segment = Segment(p_right, segment.endmark_right.get_center(), color=GREEN)
                                self.player[project_to].append(right_segment)
                                self.add(self.player[project_to][i+1])
                                #print(len(self.player[project_to]))
                        break
                        # cut_segment_end_number = i
                        
                    else:
                        if segment.endmark_right.get_center()[0] > p_right[0] + 0.1:
                            new_segment = Segment(p_left, p_right, color=self.player[project_from[0]][project_from[1]].line.get_color())
                            self.player[project_to].insert(i+1, new_segment)
                            self.add(self.player[project_to][i+1])
                            right_segment = Segment(p_right, segment.endmark_left.get_center(), color=GREEN)
                            self.player[project_to].insert(i+2, right_segment)
                            # cut_segment_end_number = i
                            break                             

                    verifying = True


                if segment.endmark_right.get_center()[0] > p_right[0] + 0.1 and verifying:

                    to_remove.add(segment)
                    # cut_segment_end_number = i
                    ##TODO
                    self.remove(segment)
                    
                    if abs(p_right[0] - segment.endmark_left.get_center()[0]) < 0.1:
                        color = segment.line.get_color()
                        text = segment.text
                    
                    else:
                        color = GREEN
                        text = False
                        #color=self.player[project_from[0]][project_from[1]].line.get_color()
                    new_segment = Segment(p_left, p_right, color=self.player[project_from[0]][project_from[1]].line.get_color())
                    right_segment = Segment(p_right, segment.endmark_right.get_center(), color=color, text=text)
                    self.player[project_to][cut_segment_start_number + 1] = new_segment
                    self.add(self.player[project_to][cut_segment_start_number + 1])
                    if i == len(self.player[project_to]):
                        self.player[project_to].append(right_segment)
                        self.add(self.player[project_to][-1])

                    else:
                        self.player[project_to].insert(cut_segment_start_number + 2, right_segment)
                        self.add(self.player[project_to][cut_segment_start_number + 2])

                    break
            for i in range(cut_segment_start_number + 3, len(self.player[project_to])):
                self.player[project_to].pop(i)
            scene.remove(to_remove) 

        self.generate_target()

        if apply_to:
            for i in apply_to:
                if i != project_from[0] and i != project_to:
                    self.target.player_name[i].set_opacity(1)
                    for s in self.target.player[i]:
                        s.set_opacity(1)
        else:
            self.target.set_opacity(1)
        scene.play(MoveToTarget(self))
        scene.play(Uncreate(d_left), Uncreate(d_right), FadeOut(new_line, run_time = 1.5)) 

    def div_segment(self, scene, player, segment):
        s = self.player[player][segment]
        
        self.remove(self.player[player][segment])
        left_segment = Segment(self.player[player][segment].endmark_left.get_center(), self.player[player][segment].get_center())
        right_segment = Segment(self.player[player][segment].get_center(), self.player[player][segment].endmark_right.get_center() )
        self.player[player][segment] = left_segment
        self.player[player].insert(segment+1, right_segment)
        
        self.add(self.player[player][segment], self.player[player][segment+1])
        scene.play(FadeIn(VGroup(self.player[player][segment], self.player[player][segment+1])))
        scene.remove(s)

              

    def update_segment_text(
        self,
        segment_index: list[int],
        text: MathTex or DecimalNumber
    ):
        [i, j] = segment_index
        self.remove(self.player[i][j])
        self.player[i][j].set_text(text)
        self.add(self.player[i][j])

    def update_length(
        self,
        scene: Scene,
        length_list: list,
        time = 1
    ):
        
        start_and_end_points: List = []
        assert len(length_list) == len(self.player), "Length of 'length_list' must match length of 'self.player'"
        for i in range(len(self.player)):
            start_and_end_points.append([[]])
            assert len(length_list[i]) == len(self.player[i]), f"Length of 'length_list[{i}]' must match length of 'self.player[{i}]'"
            start_and_end_points[i][0] = self.player[i][0].endmark_left.get_center()
            pointer = start_and_end_points[i][0][0]
            for j in range(len(self.player[i])):
                x = length_list[i][j] * self.scale_ratio/1000 + pointer
                y = start_and_end_points[i][0][1]
                z = start_and_end_points[i][0][2]
                pointer = x
                
                #if j != len(self.player[i]):
                #    start_and_end_points[i][j] = [x, y, z]
                #else:
                start_and_end_points[i].append([x, y, z])
                #start_and_end_points[i][j].np.append(x)
                #start_and_end_points[i][j].np.append(y)
                #start_and_end_points[i][j].np.append(z)
                #self.remove(self.player[i][j])


                #l = Line(self.player[i][j].endmark_left.get_center(), self.player[i][j].endmark_right.get_center())
                self.player[i][j].add_line_updater()
                self.player[i][j].add_text_updater()
                #self.add(self.player[i][j])
                scene.add(self.player[i][j].line)


        move_to_list = []
        for i in range(len(self.player)):
            for j in range(len(self.player[i])):
                [x_0, y_0, z_0] = start_and_end_points[i][j]
                [x_1, y_1, z_1] = start_and_end_points[i][j+1]
                #animation_left = self.player[i][j].endmark_left.animate.move_to(start_and_end_points[i][j])
                #animation_right = self.player[i][j].endmark_right.animate.move_to(start_and_end_points[i][j+1])
                move_to_list.append(self.player[i][j].endmark_left.animate.move_to(start_and_end_points[i][j]))
                move_to_list.append(self.player[i][j].endmark_right.animate.move_to(start_and_end_points[i][j+1]))
                
                #scene.play(self.player[i][j].endmark_left.animate.move_to([x_0, y_0, z_0]),
                #           self.player[i][j].endmark_right.animate.move_to([x_1, y_1, z_1]))
                #scene.add(self.player[i][j].line)
        scene.play(*move_to_list, run_time = time)
        for i in range(len(self.player)):
            for j in range(len(self.player[i])):
                self.player[i][j].remove_updater()
                self.add(self.player[i][j])
                scene.add(self.player[i][j].endmark_left, self.player[i][j].endmark_right)


    def integrate(
        self,
        scene: Scene,
        player: int,
        text = False
    ):    
        assert player < len(self.player), "player number out of range"
        segment_start = self.player[player][0]
        segment_end = self.player[player][-1]
        new_segment = Segment(segment_start.endmark_left.get_center(), segment_end.endmark_right.get_center(), text=text)
        scene.play(*[ReplacementTransform(segment.text, new_segment.text) for segment in self.player[player]],
                   FadeIn(new_segment.line), FadeIn(new_segment.endmark_left), FadeIn(new_segment.endmark_right))
        scene.play(*[FadeOut(VGroup(segment.line, segment.endmark_left, segment.endmark_right)) for segment in self.player[player]])

        self.remove(*[segment for segment in self.player[player]])
        
        self.add(new_segment)
        self.player[player].clear()
        self.player[player].append(new_segment)


    def group(
        self,
        scene: Scene,
        number: int
    ):
        scene.play(
            self.player_name[number].animate.shift(0.5*DOWN), self.player_name[number + 1].animate.shift(0.5*UP),
            VGroup(*[segment for segment in self.player[number]]).animate.shift(0.2*DOWN),
            VGroup(*[segment for segment in self.player[number + 1]]).animate.shift(0.2*UP)
        )


    def reorder(
        self,
        scene: Scene,
        player: int,
        order: list[int]
    ):
        # scene.play(
        #     AnimationGroup(
        #         *[self.player[player][i].animate.shift(0.25*UP*(2*order[i]/n - 1)) for i in range(len(self.player[player]))],
        #         lag_ratio=0.2
        #     )
        # )

        n = max(order)
        group_list=[]
        
        for i in range(n+1):
            group_list.append(VGroup())
            for j in range(len(self.player[player])):
    
                if order[j] == i:
                    
                    group_list[i].add(self.player[player][j])

        scene.play(
            AnimationGroup(
                *[group_list[i].animate.shift(0.25*(2*order[i]/n - 1)*UP) for i in range(n+1)],
                lag_ratio=0.2
            )
        )
        for i in range(n+1):
            print(0.25*(2*order[i]/n - 1))
        for i in range(n+1):
            group_list[i].generate_target()
            group_list[i].target.arrange(RIGHT, buff = 0)
            for s in group_list[i].target:
                s.align_to(group_list[i], DOWN)
            
            if i == 0:

                group_list[i].target.align_to(self.player[player][0], LEFT)
            else:
                group_list[i].target.align_to(group_list[i-1].target[-1].endmark_right, LEFT)
        
        scene.play(
            AnimationGroup(
                *[MoveToTarget(group_list[i]) for i in range(n+1)],
                lag_ratio=0.2
            )
        )
        scene.play(
            AnimationGroup(
                *[group_list[i].animate.shift(0.25*(2*order[i]/n - 1)*DOWN) for i in range(n+1)],
                lag_ratio=0.2
            )
        )

        help_list = []

        start_index = 0
        group_index = 0
        for i in range(len(self.player[player])+n+1):
            if start_index < len(group_list[group_index]):
                help_list.append(group_list[group_index][start_index])
                #print(order[group_index])
            else:
                group_index += 1
                start_index = -1
            start_index +=1

        self.player[player] = [s for s in help_list]




