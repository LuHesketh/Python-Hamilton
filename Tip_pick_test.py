
Created on Tue Jan 17 09:18:09 2023

@author: Luiza

import pyhamilton
from pyhamilton import (HamiltonInterface,  LayoutManager, 
 Plate96, Tip96, initialize, tip_pick_up, tip_eject, oemerr, resource_list_with_prefix)

class TipRack:
 
    def __init__(self, rack):
        self.rack = rack
        self.starting_tips = rack._num_items
        self.remaining_tips = rack._num_items
    
    def get_tips(self, num_tips):
        current_tip = self.starting_tips - self.remaining_tips
        tips_list = [(self.rack, tip) for tip in range(current_tip, current_tip + num_tips)]
        self.remaining_tips -= num_tips
        return tips_list
    
    def get_tips_seq(self, seq):
        num_tips = len([ch for ch in seq.aspirate if ch])
        tips = self.get_tips(num_tips)
        return tips



lmgr = LayoutManager('deck.lay')
tips_res = lmgr.assign_unused_resource(ResourceType(Tip96, 'tips_300'))
plates = resource_list_with_prefix(lmgr, 'plate_', Plate96, 5)
tips = resource_list_with_prefix(lmgr, 'tips', Tip96, 5)


tips_poss = [(tips[0], x) for x in range(8)]


if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        initialize(ham_int)
        tip_pick_up(ham_int, tips_poss)
        tip_eject(ham_int, tips_poss)
