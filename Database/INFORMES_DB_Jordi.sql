/**Esto es la prueba de los informes usando la DB que nos ha dado el Jordi, cuando llegue el momento tocara adaptarlo a la nuestra**/
use siete_y_medio;
/**2) Jugador que realiza la apuesta más alta en cada partida, es el que haya hecho la apuesta más alta en alguna de las rondas de la
partida.**/
/*DONE*/
select DISTINCT cardgame_id, player_id, bet_points from player_game_round pgr
where bet_points = (select max(bet_points) from player_game_round
					where cardgame_id = pgr.cardgame_id);

/**3) Jugador que realiza la apuesta más baja por partida.**/
/*DONE*/
select DISTINCT cardgame_id, player_id, bet_points from player_game_round pgr
where bet_points = (select min(bet_points) from player_game_round
					where cardgame_id = pgr.cardgame_id);

/**5) Lista de partidas ganadas por Bots. El ganador es quien ha
conseguido más puntos al finalizar la partida, los puntos
conseguidos son la diferencia entre los puntos que tenía al iniciar
la partida y los puntos al acabar.**/


/**7) Cuántos usuarios han sido la banca en cada partida.**/
/**DONE**/
select cr.cardgame_id, count(distinct player_id) from cardgame cr 
join player_game_round pgr on cr.cardgame_id = pgr.cardgame_id
where is_bank = True
group by pgr.cardgame_id;

/**8) Calcular la apuesta media por partida **/
/**DONE**/
select card.cardgame_id, sum(bet_points)/count(*) from cardgame card
join player_game_round pgr on pgr.cardgame_id = card.cardgame_id
group by card.cardgame_id;

/**9) Calcular la apuesta media de la primera ronda de cada partida.**/
/**DONE**/
select cardgame_id, avg(bet_points) from player_game_round
where round_num = 0
group by cardgame_id;

/**10) Calcular la apuesta media de la última ronda de cada partida. Los datos a mostrar son:**/
/**DONE**/
select pgr.cardgame_id, avg(bet_points) from player_game_round pgr
where round_num = (select max(round_num) from player_game_round where cardgame_id = pgr.cardgame_id)
group by pgr.cardgame_id;

/**Select para comprovar que la quary esten correctas**/
select * from player_game;

/**CREACIÓ Y USO DE LA VISTA ranking**/
/**QUERY CREACION DE LA VISTA**/
CREATE VIEW ranking as 
select pg.player_id as "Player ID", p.player_name as "Name", 
sum(pg.ending_points-pg.starting_points) as "Earnings", 
count(pg.cardgame_id) as "Games Played", 
(sum(timestampdiff(second, cr.start_hour, cr.end_hour))/60) as "Minutes Played" from player_game pg
join player p on p.player_id = pg.player_id
join cardgame cr on cr.cardgame_id = pg.cardgame_id
group by pg.player_id;

/**QUERY PARA VER ranking**/
select * from ranking order by `Earnings` desc;
select * from ranking order by `Games Played` desc;
select * from ranking order by `Minutes Played` desc;