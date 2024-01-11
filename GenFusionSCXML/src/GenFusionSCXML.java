/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import scxmlgen.Fusion.FusionGenerator;
//import FusionGenerator;

import Modalities.Output;
import Modalities.Speech;
import Modalities.Touch;
import Modalities.Gestures;

/**
 *
 * @author nunof
 */
public class GenFusionSCXML {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {

    FusionGenerator fg = new FusionGenerator();

    // --------------------COMPLEMENTARES--------------------
    fg.Complementary(Speech.GAME_INFO_HELP, Gestures.HELP, Output.HELP_GAME_INFO);
    fg.Complementary(Speech.LIST_OF_COLORS_HELP, Gestures.HELP, Output.HELP_LIST_OF_COLORS);
    
    fg.Complementary(Gestures.ROLL_DICE, Speech.BUY_HOUSE, Output.ROLL_DICE_BUY_HOUSE);
    fg.Complementary(Speech.ROLL_DICE, Gestures.BUY_HOUSE, Output.ROLL_DICE_BUY_HOUSE);
    // fg.Complementary(Gestures.ROLL_DICE, Speech.COMPLETED, Output.ROLL_DICE_COMPLETED);

        // .......................colors........................
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_CYAN, Output.SELECT_COLOR_CYAN);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_AZUL, Output.SELECT_COLOR_AZUL);


  


    // -------------------- REDUNDANTES --------------------
    fg.Redundancy(Speech.ROLL_DICE, Gestures.ROLL_DICE, Output.ROLL_DICE);
    fg.Redundancy(Speech.BUY_HOUSE, Gestures.BUY_HOUSE, Output.BUY_HOUSE);
    fg.Redundancy(Speech.END_TURN, Gestures.END_TURN, Output.END_TURN);
    fg.Redundancy(Speech.GIVE_UP_GAME, Gestures.GIVE_UP_GAME, Output.GIVE_UP_GAME);



    // --------------------SINGLE--------------------
    fg.Single(Speech.GAME_INFO_HELP, Output.GAME_INFO);
    fg.Single(Speech.LIST_OF_COLORS_HELP, Output.LIST_OF_COLORS);
    fg.Single(Gestures.SELECT, Output.SELECT);
        // .......................colors........................
    fg.Single(Speech.CHOOSE_COLOR_CYAN, Output.CHOOSE_COLOR_CYAN);
    fg.Single(Speech.CHOOSE_COLOR_AZUL, Output.CHOOSE_COLOR_AZUL);


  

    // --------------------BUILD--------------------
    fg.Build("fusion.scxml");
        
    }
    
}
