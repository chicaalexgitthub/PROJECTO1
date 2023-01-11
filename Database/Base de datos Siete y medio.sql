/*Creacio de la Base de dades*/
DROP DATABASE IF EXISTS seven_half;
CREATE DATABASE seven_half CHARACTER SET utf8mb4;

/*Creació de les diferents taules*/
use seven_half;
create table player (
	player_id varchar(25) primary key,
    player_name varchar(40) not null,
    player_risk tinyint,
    human tinyint(1)
);

create table deck (
	deck_id int primary key,
    deck_name varchar(25)
);

create table cardgame (
	cardgame_id int primary key,
    players tinyint,
    rounds tinyint,
    start_hour datetime,
    end_hour datetime,
    deck_id int,
    foreign key (deck_id) references deck(deck_id)
);

create table card (
	card_id char(3) primary key,
    card_name varchar(25),
    card_value decimal (3,1),
    card_suit varchar(25),
    card_priority tinyint,
    card_real_value tinyint,
    deck_id int,
    foreign key (deck_id) references deck(deck_id)
);

create table player_game (
	cardgame_id int,
    player_id varchar(25),
    
    /**Preguntar a la profe como relacionar initial_card_id con la otra tabla | **/
    initial_card_id char(3),
    starting_points tinyint,
    ending_points tinyint,
    
    primary key (cardgame_id, player_id),
    unique index (cardgame_id, player_id),
    
    foreign key (cardgame_id) references cardgame(cardgame_id),
    foreign key (player_id) references player(player_id)
);

create table playe_game_round (
	round_num tinyint,
	cardgame_id int,
    player_id varchar(25),
    
    is_bank tinyint(1),
    bet_points tinyint,
    card_value decimal(4,1),
    starting_round_points tinyint,
    ending_round_points tinyint,
    
    /**Preguntar si esto es correcto para lo que quiero hacer**/
    primary key (round_num, cardgame_id, player_id),
    
    foreign key (cardgame_id) references cardgame(cardgame_id),
    foreign key (player_id) references player(player_id)
);