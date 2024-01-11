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
    fg.Complementary(Gestures.ROLL_DICE, Speech.COMPLETED, Output.ROLL_DICE_COMPLETED);

        // .......................colors........................
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_CYAN, Output.SELECT_COLOR_CYAN);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_AZUL, Output.SELECT_COLOR_AZUL);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_LIME, Output.SELECT_COLOR_LIME);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_YELLOW, Output.SELECT_COLOR_YELLOW);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_ORANGE, Output.SELECT_COLOR_ORANGE);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_RED, Output.SELECT_COLOR_RED);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_BLUE, Output.SELECT_COLOR_BLUE);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_WATER, Output.SELECT_COLOR_WATER);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_GREEN, Output.SELECT_COLOR_GREEN);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_BROWN, Output.SELECT_COLOR_BROWN);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_HOTPINK, Output.SELECT_COLOR_HOTPINK);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_PURPLE, Output.SELECT_COLOR_PURPLE);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_PINK, Output.SELECT_COLOR_PINK);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_AMARELO, Output.SELECT_COLOR_AMARELO);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_LARANJA, Output.SELECT_COLOR_LARANJA);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_VERMELHO, Output.SELECT_COLOR_VERMELHO);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_CIANO, Output.SELECT_COLOR_CIANO);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_VERDE, Output.SELECT_COLOR_VERDE);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_MARROM, Output.SELECT_COLOR_MARROM);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_ROSA, Output.SELECT_COLOR_ROSA);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_ROXO, Output.SELECT_COLOR_ROXO);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_AGUA, Output.SELECT_COLOR_AGUA);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_CASTANHO, Output.SELECT_COLOR_CASTANHO);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_MAGENTA, Output.SELECT_COLOR_MAGENTA);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_CASTANHA, Output.SELECT_COLOR_CASTANHA);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_VERDE_LIMA, Output.SELECT_COLOR_VERDE_LIMA);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_VERMELHA, Output.SELECT_COLOR_VERMELHA);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_AMAERELA, Output.SELECT_COLOR_AMAERELA);
    fg.Complementary(Gestures.SELECT, Speech.CHOOSE_COLOR_ROXA, Output.SELECT_COLOR_ROXA);



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
    fg.Single(Speech.CHOOSE_COLOR_LIME, Output.CHOOSE_COLOR_LIME);
    fg.Single(Speech.CHOOSE_COLOR_YELLOW, Output.CHOOSE_COLOR_YELLOW);
    fg.Single(Speech.CHOOSE_COLOR_ORANGE, Output.CHOOSE_COLOR_ORANGE);
    fg.Single(Speech.CHOOSE_COLOR_RED, Output.CHOOSE_COLOR_RED);
    fg.Single(Speech.CHOOSE_COLOR_BLUE, Output.CHOOSE_COLOR_BLUE);
    fg.Single(Speech.CHOOSE_COLOR_WATER, Output.CHOOSE_COLOR_WATER);
    fg.Single(Speech.CHOOSE_COLOR_GREEN, Output.CHOOSE_COLOR_GREEN);
    fg.Single(Speech.CHOOSE_COLOR_BROWN, Output.CHOOSE_COLOR_BROWN);
    fg.Single(Speech.CHOOSE_COLOR_HOTPINK, Output.CHOOSE_COLOR_HOTPINK);
    fg.Single(Speech.CHOOSE_COLOR_PURPLE, Output.CHOOSE_COLOR_PURPLE);
    fg.Single(Speech.CHOOSE_COLOR_PINK, Output.CHOOSE_COLOR_PINK);
    fg.Single(Speech.CHOOSE_COLOR_AMARELO, Output.CHOOSE_COLOR_AMARELO);
    fg.Single(Speech.CHOOSE_COLOR_LARANJA, Output.CHOOSE_COLOR_LARANJA);
    fg.Single(Speech.CHOOSE_COLOR_VERMELHO, Output.CHOOSE_COLOR_VERMELHO);
    fg.Single(Speech.CHOOSE_COLOR_CIANO, Output.CHOOSE_COLOR_CIANO);
    fg.Single(Speech.CHOOSE_COLOR_VERDE, Output.CHOOSE_COLOR_VERDE);
    fg.Single(Speech.CHOOSE_COLOR_MARROM, Output.CHOOSE_COLOR_MARROM);
    fg.Single(Speech.CHOOSE_COLOR_ROSA, Output.CHOOSE_COLOR_ROSA);
    fg.Single(Speech.CHOOSE_COLOR_ROXO, Output.CHOOSE_COLOR_ROXO);
    fg.Single(Speech.CHOOSE_COLOR_AGUA, Output.CHOOSE_COLOR_AGUA);
    fg.Single(Speech.CHOOSE_COLOR_CASTANHO, Output.CHOOSE_COLOR_CASTANHO);
    fg.Single(Speech.CHOOSE_COLOR_MAGENTA, Output.CHOOSE_COLOR_MAGENTA);
    fg.Single(Speech.CHOOSE_COLOR_CASTANHA, Output.CHOOSE_COLOR_CASTANHA);
    fg.Single(Speech.CHOOSE_COLOR_VERDE_LIMA, Output.CHOOSE_COLOR_VERDE_LIMA);
    fg.Single(Speech.CHOOSE_COLOR_VERMELHA, Output.CHOOSE_COLOR_VERMELHA);
    fg.Single(Speech.CHOOSE_COLOR_AMAERELA, Output.CHOOSE_COLOR_AMAERELA);
    fg.Single(Speech.CHOOSE_COLOR_ROXA, Output.CHOOSE_COLOR_ROXA);


    // --------------------BUILD--------------------
    fg.Build("fusion.scxml");
        
    }
    
}
