insert into move (name, lower_damage_range, upper_damage_range)
values
("normal punch", '500', '1000'),
("chop", '100', '200'),
("consecutive normal punch", '5000', '20000'),
("serious punch", '100000', '300000'),
("leaf hurrican", '200', '300'),
("meteor kick", '150', '400'),
("primary lotus", '1500', '3000'),
("hidden lotus - ura renge", '4000', '6000'),
("short jab", '500', '1000'),
("stone throw", '10', '100'),
("solar flare", '0', '1'),
("destructo-disc", '10000', '40000'),
("lariat", '300', '500'),
("lightning beast fang", '400', '700'),
("thunderbolt", '1000', '1200'),
("chidori", '2500', '5000'),
("headbutt", '1000', '1500'),
("typhoon", '2000', '2300'),
("blind meteor", '3000', '4000'),
("big blaster", '7000', '8000');

insert into computer_fighter(name, health_points, move_one, move_two, move_three, move_four)
values
('A Random Lightning Shinobi', '1000', '13', '14', '15', '16')
('A Pink Dodoria', '20000', '17', '18', '19', '20');

call create_account('test_user_1', 'pw123');

select id from client
where username = 'test_user_1' and password = 'pw123';

call checking_credentials ('test_user_1', 'pw123');

call configuring_player ('1', '1', '2', '3', '4');