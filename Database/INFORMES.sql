use seven_half;
/**INFORMES**/
/**1) Carta inicial más repetida por cada jugador, solo se tienen en
cuenta jugadores que hayan jugado un mínimo de 3 partidas.**/

/**8) Calcular la apuesta media por partida**/
select card.cardgame_id, sum(bet_points)/count(*) from cardgame card
join player_game_round pgr on pgr.cardgame_id = card.cardgame_id
group by card.cardgame_id;
