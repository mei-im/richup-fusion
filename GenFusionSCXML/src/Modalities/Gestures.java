/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modalities;

import scxmlgen.interfaces.IModality;


public enum Gestures implements IModality{


    // ----------------REDUDANTES----------------
    ROLL_DICE("[GESTURES][HANDONEDIRECTIONROLLDICE]", 5000),
    BUY_HOUSE("[GESTURES][HANDSJOIN]", 5000),
    END_TURN("[GESTURES][HANDSDIFFERENTDIRECTIONSCLOSE]", 3000),
    GIVE_UP_GAME("[GESTURES][HANDSUPGIVEUP]", 3000),

    // ----------------COMPLEMENTARES----------------
    HELP("[GESTURES][HANDRIGHTUPHELP]", 5000),
    SELECT("[GESTURES][HANDSFRONTSELECT]", 5000),

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