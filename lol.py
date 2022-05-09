import wrap


wrap.world.create_world(1000,700)

wrap.add_sprite_dir("vechaslavtop")

pervey = wrap.sprite.add("daed",500,500, "kvadrat_1")

@wrap.always()
def polet_pryamougolnik_1 ():
    global pervey
    bottom=wrap.sprite.get_bottom(pervey)

    if bottom<695 :
        wrap.sprite.move(pervey, 0, +5)
        bottom = wrap.sprite.get_bottom(pervey)
    gradus = wrap.sprite.get_angle(pervey)
    if  gradus==90 :
        if bottom>695:
            wrap.sprite.move_to(pervey,500,668)



@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def povorot_perve ():

    gradus=wrap.sprite.get_angle(pervey)
    gradus+=90
    wrap.sprite.set_angle(pervey,gradus)
    bottom=wrap.sprite.get_bottom(pervey)
    if bottom>695:
        gradus-=90
        wrap.sprite.set_angle(pervey, gradus)


# сначала ми его поварачиваем  +90
# проверяем боттом
# проверяяем зошла ли он за граници экрана
# если она зошла то тогда возращаем обратно


# @wrap.on_mouse_down(wrap.BUTTON_RIGHT)
# def povorot_perve():
#     gradus = wrap.sprite.get_angle(pervey)
#
#     gradus+=90
#     wrap.sprite.set_angle(pervey, gradus)




import wrap_py
wrap_py.app.start()
