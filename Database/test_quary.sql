use seven_half;
/*TABLE deck*/
select * from deck;
INSERT INTO deck VALUES (2, "Poker Deck");

/**TABLE card*/
/**Bastos B, Copas C, Espadas E, Oros O**/
/**Treboles T | Diamantes D | Corazones H | Picas P --- Jota J | Reina Q | Rey K **/
select count(*) from card where deck_id = 2 and card_value = 0.5;

select * from card order by deck_id, card_id;
/**TABLE Player**/
select * from player;

/**TABLE cardgame**/
select cardgame_id from cardgame;
