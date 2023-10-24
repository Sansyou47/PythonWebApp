
# テーブルemployeeの作成
create table employee(
	number	int auto_increment primary key,
	name	varchar(50) not null,
	category	varchar(50) not null,
	auth	int not null,
	gender	varchar(20),
	start	int not null,
	finish	int not null,
	pass	varchar(3000)
) auto_increment = 123200;

# テーブルemployeeへデータを入力
insert into employee(name, category, auth, gender, start, finish, pass)
	values('嫁阪雄大', '店長', 0, 'male', 18, 21, 'None');
insert into employee(name, category, auth, gender, start, finish, pass)
	values('木下秀吉', '副店長', 1, 'male', 8, 17, 'None');
insert into employee(name, category, auth, gender, start, finish, pass)
	values('飯野美沙', '副店長', 1, 'female', 12, 21, 'None');
insert into employee(name, category, auth, gender, start, finish, pass)
	values('富士富雄', '管理', 2, 'male', 12, 21, 'None');
insert into employee(name, category, auth, gender, start, finish, pass)
	values('大空スバル', 'レジ統合', 2, 'female', 17, 21, 'None');
insert into employee(name, category, auth, gender, start, finish, pass)
	values('岸辺露伴', '書籍', 2, 'male', 8, 15, 'None');

# holidayテーブルの作成
drop table if exists holiday;
create table holiday (
	number	int auto_increment primary key,
	id		int,
	date	date not null,
	type	varchar(50) not null,
	status	int default 2 not null,
	regtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
