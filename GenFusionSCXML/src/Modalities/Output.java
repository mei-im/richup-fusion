package Modalities;

import scxmlgen.interfaces.IOutput;

public enum Output implements IOutput{
    // -------------------------CORES-------------------------
    CHOOSE_COLOR_LIME("[FUSION][CHOOSE_COLOR][LIME]"),
    CHOOSE_COLOR_YELLOW("[FUSION][CHOOSE_COLOR][YELLOW]"),
    CHOOSE_COLOR_ORANGE("[FUSION][CHOOSE_COLOR][ORANGE]"),
    CHOOSE_COLOR_RED("[FUSION][CHOOSE_COLOR][RED]"),
    CHOOSE_COLOR_BLUE("[FUSION][CHOOSE_COLOR][BLUE]"),
    CHOOSE_COLOR_CYAN("[FUSION][CHOOSE_COLOR][CYAN]"),
    CHOOSE_COLOR_WATER("[FUSION][CHOOSE_COLOR][WATER]"),
    CHOOSE_COLOR_GREEN("[FUSION][CHOOSE_COLOR][GREEN]"),
    CHOOSE_COLOR_BROWN("[FUSION][CHOOSE_COLOR][BROWN]"),
    CHOOSE_COLOR_HOTPINK("[FUSION][CHOOSE_COLOR][HOTPINK]"),
    CHOOSE_COLOR_PURPLE("[FUSION][CHOOSE_COLOR][PURPLE]"),
    CHOOSE_COLOR_PINK("[FUSION][CHOOSE_COLOR][PINK]"),
    CHOOSE_COLOR_AMARELO("[FUSION][CHOOSE_COLOR][AMARELO]"),
    CHOOSE_COLOR_LARANJA("[FUSION][CHOOSE_COLOR][LARANJA]"),
    CHOOSE_COLOR_VERMELHO("[FUSION][CHOOSE_COLOR][VERMELHO]"),
    CHOOSE_COLOR_AZUL("[FUSION][CHOOSE_COLOR][AZUL]"),
    CHOOSE_COLOR_CIANO("[FUSION][CHOOSE_COLOR][CIANO]"),
    CHOOSE_COLOR_VERDE("[FUSION][CHOOSE_COLOR][VERDE]"),
    CHOOSE_COLOR_MARROM("[FUSION][CHOOSE_COLOR][MARROM]"),
    CHOOSE_COLOR_ROSA("[FUSION][CHOOSE_COLOR][ROSA]"),
    CHOOSE_COLOR_ROXO("[FUSION][CHOOSE_COLOR][ROXO]"),
    CHOOSE_COLOR_AGUA("[FUSION][CHOOSE_COLOR][ÁGUA]"),
    CHOOSE_COLOR_AZUL_AGUA("[FUSION][CHOOSE_COLOR][AGUA]"),
    CHOOSE_COLOR_CASTANHO("[FUSION][CHOOSE_COLOR][CASTANHO]"),
    CHOOSE_COLOR_MAGENTA("[FUSION][CHOOSE_COLOR][MAGENTA]"),
    CHOOSE_COLOR_CASTANHA("[FUSION][CHOOSE_COLOR][CASTANHA]"),
    CHOOSE_COLOR_VERDE_LIMA("[FUSION][CHOOSE_COLOR][VERDE_LIMA]"),
    CHOOSE_COLOR_VERMELHA("[FUSION][CHOOSE_COLOR][VERMELHA]"),
    CHOOSE_COLOR_AMAERELA("[FUSION][CHOOSE_COLOR][AMAERELA]"),
    CHOOSE_COLOR_ROXA("[FUSION][CHOOSE_COLOR][ROXA]"),


    // -------------------------REDUNDANTES-------------------------
    ROLL_DICE("[FUSION][ROLL_DICE]"),
    BUY_HOUSE("[FUSION][BUY_HOUSE]"),
    END_TURN("[FUSION][END_TURN]"),
    GIVE_UP_GAME("[FUSION][GIVE_UP_GAME]"),
    // ------------------------ SINGLE ----------------------
    HELP("[FUSION][HELP]"),

    // -------------------------COMPLEMENTARES-------------------------
    HELP_GAME_INFO("[FUSION][HELP_GAME_INFO]"),
    HELP_LIST_OF_COLORS("[FUSION][HELP_LIST_OF_COLORS]"),


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
