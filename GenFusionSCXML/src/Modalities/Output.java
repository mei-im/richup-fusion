package Modalities;

import scxmlgen.interfaces.IOutput;

public enum Output implements IOutput{
    // -------------------------REDUNDANTES-------------------------
    ROLL_DICE("[FUSION][ROLL_DICE]"),
    BUY_HOUSE("[FUSION][BUY_HOUSE]"),
    END_TURN("[FUSION][END_TURN]"),
    GIVE_UP_GAME("[FUSION][GIVE_UP_GAME]"),
    
    // ------------------------ SINGLE ----------------------
    HELP("[FUSION][HELP]"),
    LIST_OF_COLORS("[FUSION][LIST_OF_COLORS]"),
    GAME_INFO("[FUSION][GAME_INFO]"),

    // -------------------------COMPLEMENTARES-------------------------
    HELP_GAME_INFO("[FUSION][HELP_GAME_INFO]"),
    HELP_LIST_OF_COLORS("[FUSION][HELP_LIST_OF_COLORS]"),
    ROLL_DICE_BUY_HOUSE("[FUSION][ROLL_DICE_BUY_HOUSE]"),


    ;
    
    
    
    private String event;

    Output(String m) {
        event=m;
    }
    
    public String getEvent(){
        return this.toString();
    }

    public String getEventName(){
        return event;
    }
}
