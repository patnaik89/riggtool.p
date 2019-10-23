import maya.cmds as cmds

# INTERFACE

window_name="rigg_tool"
window_title="Simple Rigg"
window_w=200
window_h=200


def create_window():  
    if cmds.window(window_name,query=True, exists=True):
        cmds.deleteUI(window_name)
    cmds.window(window_name)
    cmds.window(window_name, edit=True, w=window_w+2, h=window_h, title=window_title, mnb=False, mxb=False, s=False)
    
    cmds.columnLayout("main_column", w=window_w, h=window_h)
    create_customUI()
    
    cmds.showWindow(window_name)
    
def create_customUI():
    cmds.button("rigg_button", label="Rigg", w=window_w, h=40)
    
    cmds.frameLayout("control_scale frame", label="control Scale", w=window_w, parent="main_column", bgc=(0.5,0.5,0.0))
    cmds.rowLayout("control_scale_row", nc=3, w=window_w)
    
    cmds.floatField(precision=2, w= window_w/3)
    cmds.button("small_button", label="Small", w=window_w/3)
    cmds.button("bugg_button", label="Big", w=window_w/3)
    
    cmds.frameLayout("control_color_frame", label="control color", w=window_w, parent="main_column")
    cmds.colorIndexSliderGrp(max=20, value=18)
    cmds.button("set_color", label="set color", h=30)
    

                 
                
create_window()
