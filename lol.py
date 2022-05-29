import random

import wrap


wrap.world.create_world(1000 ,700)

wrap.add_sprite_dir("vechaslavtop")

pervey=None
spisokperveh=[]
# pervey = wrap.sprite.add("mario-1-small",500,500, "climb2")

def randon_kartinka():
    global pervey
    what=random.randint(1,7)
    if what==1:
        pervey = wrap.sprite.add("daed",500,-200, "kvadrat_1")
    if what==2:
        pervey = wrap.sprite.add("daed", 500,-200, "kvadrat_2")
    if what==3:
        pervey = wrap.sprite.add("daed", 500, -200, "kvadrat_3")
    if what==4:
        pervey = wrap.sprite.add("daed", 500, -200, "kvadrat_4")
    if what==5:
        pervey = wrap.sprite.add("daed", 500, -200, "kvadrat_5")
    if what==6:
        pervey = wrap.sprite.add("daed", 500, -200, "kvadrat_6")
    if what==7:
        pervey = wrap.sprite.add("daed", 500, -200, "kvadrat_7")




    bottom=wrap.sprite.get_bottom(pervey)
    if bottom>500 :
        bottom=wrap.sprite.get_bottom(pervey)

    if bottom>690  :
        spisokperveh.append(pervey)
    print(spisokperveh)

@wrap.always()
def polet_pryamougolnik_1 ():
    global pervey

    if pervey== None:
        randon_kartinka()

    bottom=wrap.sprite.get_bottom(pervey)

    for  did in spisokperveh :
        ses = wrap.sprite.is_collide_sprite(pervey,did)
        if ses==True:
            randon_kartinka()




    wrap.sprite.move(pervey, 0, +25)

    if bottom>695:
        wrap.sprite.move_bottom_to(pervey,695)
        randon_kartinka()
        print("лох")
        spisokperveh.append(pervey)
        print(spisokperveh)


@wrap.on_mouse_down(wrap.BUTTON_LEFT )
def povorot_perve ():

    gradus=wrap.sprite.get_angle(pervey)
    gradus+=90
    wrap.sprite.set_angle(pervey,gradus)
    bottom=wrap.sprite.get_bottom(pervey)
    if bottom>700:
        gradus-=90
        wrap.sprite.set_angle(pervey, gradus)

@wrap.on_mouse_down( wrap.BUTTON_RIGHT)
def povorot_pravo():
    gradus = wrap.sprite.get_angle(pervey)
    gradus-=90
    wrap.sprite.set_angle(pervey,gradus)
    bottom=wrap.sprite.get_bottom(pervey)
    if bottom>700:
        gradus += 90
        wrap.sprite.set_angle(pervey, gradus)



@wrap.always()
def povorot_pravo(keys):
    if pervey==None:
        return
    x = wrap.sprite.get_x(pervey)
    y = wrap.sprite.get_y(pervey)
    bottom=wrap.sprite.get_bottom(pervey)
    if  bottom<699 :
        if wrap.K_a in keys:
            x-=10

        if wrap.K_d in keys:
            x+=10
        wrap.sprite.move_to(pervey,x,y)


# сначала ми его поварачиваем  +90
# проверяем боттом
# проверяяем зошла ли он за граници экрана
# если она зошла то тогда возращаем обратно






import wrap_py
wrap_py.app.start()
