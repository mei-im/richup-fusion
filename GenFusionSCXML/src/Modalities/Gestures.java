/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modalities;

import scxmlgen.interfaces.IModality;


public enum Gestures implements IModality{


    // ----------------REDUDANTES----------------
    ROLL_DICE("[GESTURES][HANDONEDIRECTIONROLLDICE]", 1500),
    BUY_HOUSE("[GESTURES][HANDSJOIN]", 1500),
    END_TURN("[GESTURES][HANDSDIFFERENTDIRECTIONSCLOSE]", 1500),
    GIVE_UP_GAME("[GESTURES][HANDSUPGIVEUP]", 1500),

    // ----------------COMPLEMENTARES----------------
    HELP("[GESTURES][HANDRIGHTUPHELP]", 1500),

    ;
    
    private String event;
    private int timeout;


    Gestures(String m, int time) {
        event=m;
        timeout=time;
    }

    @Override
    public int getTimeOut() {
        return timeout;
    }

    @Override
    public String getEventName() {
        //return getModalityName()+"."+event;
        return event;
    }

    @Override
    public String getEvName() {
        return getModalityName().toLowerCase()+event.toLowerCase();
    }
    
}