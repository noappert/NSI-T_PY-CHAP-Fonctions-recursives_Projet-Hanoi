from classes.hanoi import *

n = input("Nbr de pièces? :> ")
setup = Hanoi(int(n))
setup.jouer()
setup.text.config(
    text="                                                            Terminé                                                            ",
    background="green",
)
setup.root.title("Hanoï : %s disque.s [FINI]" % setup.nbdisques)
setup.root.mainloop()
