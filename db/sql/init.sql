
# テーブルemployeeの作成
create table employee(
	ident	int auto_increment primary key,
	name	varchar(50) not null,
	category	varchar(50) not null,
	auth	int not null,
	number	int,
	gender	varchar(20),
	start	int not null,
	finish	int not null,
	pass	varchar(3000)
);

# テーブルemployeeへデータを入力
insert into employee(name, category, auth, number, gender, start, finish, pass)
	values('嫁阪雄大', '店長', 0, 123209, 'male', 18, 21, 'None');
insert into employee(name, category, auth, number, gender, start, finish, pass)
	values('木下秀吉', '副店長', 1, 123229, 'male', 8, 17, 'None');
insert into employee(name, category, auth, number, gender, start, finish, pass)
	values('飯野美沙', '副店長', 1, 100000, 'female', 12, 21, 'None');
insert into employee(name, category, auth, number, gender, start, finish, pass)
	values('富士富雄', '管理', 2, 000022, 'male', 12, 21, 'None');
insert into employee(name, category, auth, number, gender, start, finish, pass)
	values('大空スバル', 'レジ統合', 2, 121212, 'female', 17, 21, 'None');
insert into employee(name, category, auth, number, gender, start, finish, pass)
	values('岸辺露伴', '書籍', 2, 123210, 'male', 8, 15, 'None');


