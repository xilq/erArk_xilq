from typing import List
from types import FunctionType
from Script.Core import cache_control, game_type, get_text, flow_handle, constant
from Script.Design import handle_talent
from Script.UI.Moudle import draw
from Script.Config import game_config, normal_config
import random

cache: game_type.Cache = cache_control.cache
""" 游戏缓存数据 """
_: FunctionType = get_text._
""" 翻译api """
line_feed = draw.NormalDraw()
""" 换行绘制对象 """
line_feed.text = "\n"
line_feed.width = 1
window_width: int = normal_config.config_normal.text_width
""" 窗体宽度 """


class System_Setting_Panel:
    """
    用于系统设置的面板对象
    Keyword arguments:
    width -- 绘制宽度
    """

    def __init__(self, width: int):
        """初始化绘制对象"""
        self.width: int = width
        """ 绘制的最大宽度 """
        # self.now_panel = _("系统设置")
        # """ 当前绘制的页面 """
        self.draw_list: List[draw.NormalDraw] = []
        """ 绘制的文本列表 """
        self.pl_character_data = cache.character_data[0]
        """ 玩家的属性 """

    def draw(self):
        """绘制对象"""

        title_text = "系统设置"
        title_draw = draw.TitleLineDraw(title_text, self.width)
        while 1:
            return_list = []
            title_draw.draw()

            button_text = f"[001]主界面每次刷新时的空行数量："
            now_line_count = cache.system_setting.line_before_main_update
            button_text += f"[{now_line_count}行]"
            button_draw = draw.LeftButton(
                _(button_text),
                _("1"),
                window_width,
                cmd_func=self.line_before_main_update,
                )
            line_feed.draw()
            button_draw.draw()
            return_list.append(button_draw.return_text)

            button_text = f"[002]是否在博士入睡结算时自动升级玩家的能力："
            if cache.system_setting.pl_ability_auto_lvup:
                draw_text = _("[是]")
            else:
                draw_text = _("[否]")
            button_text += f"{draw_text}"
            button_draw = draw.LeftButton(
                _(button_text),
                _("2"),
                window_width,
                cmd_func=self.change_pl_ability_auto_lvup,
                )
            line_feed.draw()
            button_draw.draw()
            return_list.append(button_draw.return_text)

            button_text = f"[003]是否在博士入睡结算时自动升级干员的能力："
            if cache.system_setting.npc_ability_auto_lvup:
                draw_text = _("[是]")
            else:
                draw_text = _("[否]")
            button_text += f"{draw_text}"
            button_draw = draw.LeftButton(
                _(button_text),
                _("3"),
                window_width,
                cmd_func=self.change_npc_ability_auto_lvup,
                )
            line_feed.draw()
            button_draw.draw()
            return_list.append(button_draw.return_text)

            button_text = f"[004]每次射精时手动选择射在哪里："
            if cache.system_setting.choose_shoot_where:
                draw_text = _("[是]")
            else:
                draw_text = _("[否，自动射在当前阴茎所在的位置]")
            button_text += f"{draw_text}"
            button_draw = draw.LeftButton(
                _(button_text),
                _("4"),
                window_width,
                cmd_func=self.change_choose_shoot_where,
                )
            line_feed.draw()
            button_draw.draw()
            return_list.append(button_draw.return_text)

            button_text = f"[005]博士的尿意值自然增长(优先于6号的速度判定)："
            if cache.system_setting.dr_need_pee:
                draw_text = _("[是]")
            else:
                draw_text = _("[否，博士的尿意值不再自然增加]")
            button_text += f"{draw_text}"
            button_draw = draw.LeftButton(
                _(button_text),
                _("5"),
                window_width,
                cmd_func=self.change_dr_need_pee,
                )
            line_feed.draw()
            button_draw.draw()
            return_list.append(button_draw.return_text)

            button_text = f"[006]全角色尿意值的增长速度："
            if cache.system_setting.urinate_grow_speed == 0:
                draw_text = _("[不自然增加]")
            elif cache.system_setting.urinate_grow_speed == 1:
                draw_text = _("[慢，8h回满]")
            elif cache.system_setting.urinate_grow_speed == 2:
                draw_text = _("[中，4h回满]")
            elif cache.system_setting.urinate_grow_speed == 3:
                draw_text = _("[快，2h回满]")
            button_text += f"{draw_text}"
            button_draw = draw.LeftButton(
                _(button_text),
                _("6"),
                window_width,
                cmd_func=self.change_urinate_grow_speed,
                )
            line_feed.draw()
            button_draw.draw()
            return_list.append(button_draw.return_text)

            button_text = f"[007]是否开关精液流通功能："
            if cache.system_setting.dr_need_pee:
                draw_text = _("[是，射上去的精液会有部分流向联通部位]")
            else:
                draw_text = _("[否，精液只会停留在射上去的部位]")
            button_text += f"{draw_text}"
            button_draw = draw.LeftButton(
                _(button_text),
                _("7"),
                window_width,
                cmd_func=self.change_semen_flow,
                )
            line_feed.draw()
            button_draw.draw()
            return_list.append(button_draw.return_text)

            line_feed.draw()
            line_feed.draw()
            back_draw = draw.CenterButton(_("[返回]"), _("返回"), window_width)
            back_draw.draw()
            line_feed.draw()
            return_list.append(back_draw.return_text)
            yrn = flow_handle.askfor_all(return_list)
            if yrn == back_draw.return_text:
                cache.now_panel_id = constant.Panel.IN_SCENE
                break

    def line_before_main_update(self):
        """主界面每次刷新时的空行数量"""
        while 1:
            return_list = []
            line_draw = draw.LineDraw("-", self.width)
            line_draw.draw()
            now_line_count = cache.system_setting.line_before_main_update
            info_draw = draw.NormalDraw()
            info_text = ""
            info_text += f"\n当前{now_line_count}行，行数选择："
            info_draw.text = _(info_text)
            info_draw.draw()

            for i in [1,2,3,5,10,50]:
                button_text = f" [{i}行] "
                button_draw = draw.CenterButton(button_text, button_text, len(button_text)*2, cmd_func=self.change_line_before_main_update, args=i)
                button_draw.draw()
                return_list.append(button_draw.return_text)

            line_feed.draw()
            line_feed.draw()
            back_draw = draw.CenterButton(_("[返回]"), _("返回"), window_width)
            back_draw.draw()
            line_feed.draw()
            return_list.append(back_draw.return_text)
            yrn = flow_handle.askfor_all(return_list)
            if yrn in return_list:
                break

    def change_line_before_main_update(self, line_count):
        """改变主界面每次刷新时的空行数量"""
        cache.system_setting.line_before_main_update = line_count

    def change_pl_ability_auto_lvup(self):
        """改变自动升级玩家的能力"""
        cache.system_setting.pl_ability_auto_lvup = not cache.system_setting.pl_ability_auto_lvup

    def change_npc_ability_auto_lvup(self):
        """改变自动升级干员的能力"""
        cache.system_setting.npc_ability_auto_lvup = not cache.system_setting.npc_ability_auto_lvup

    def change_choose_shoot_where(self):
        """改变每次射精时手动选择射在哪里"""
        cache.system_setting.choose_shoot_where = not cache.system_setting.choose_shoot_where

    def change_dr_need_pee(self):
        """改变博士是否需要尿尿"""
        cache.system_setting.dr_need_pee = not cache.system_setting.dr_need_pee

    def change_urinate_grow_speed(self):
        """改变全角色尿意值的增长速度"""
        while 1:
            return_list = []
            line_draw = draw.LineDraw("-", self.width)
            line_draw.draw()
            info_draw = draw.NormalDraw()
            info_text = ""
            info_text += f"\n当前全角色尿意值的增长速度："
            info_draw.text = _(info_text)
            info_draw.draw()

            for i in [0,1,2,3]:
                if i == 0:
                    button_text = f" [不自然增加] "
                elif i == 1:
                    button_text = f" [慢，8h回满] "
                elif i == 2:
                    button_text = f" [中，4h回满] "
                elif i == 3:
                    button_text = f" [快，2h回满] "
                button_draw = draw.CenterButton(button_text, button_text, len(button_text)*2, cmd_func=self.change_urinate_grow_speed_, args=i)
                button_draw.draw()
                return_list.append(button_draw.return_text)

            line_feed.draw()
            line_feed.draw()
            back_draw = draw.CenterButton(_("[返回]"), _("返回"), window_width)
            back_draw.draw()
            line_feed.draw()
            return_list.append(back_draw.return_text)
            yrn = flow_handle.askfor_all(return_list)
            if yrn in return_list:
                break

    def change_urinate_grow_speed_(self, speed):
        """改变全角色尿意值的增长速度"""
        cache.system_setting.urinate_grow_speed = speed

    def change_semen_flow(self):
        """改变精液流通功能"""
        cache.system_setting.semen_flow = not cache.system_setting.semen_flow
