use pytest

# テーブル employee の作成
drop table if exists ; 
# テーブルemployeeの作成
create table employee(
	ident	int auto_increment primary key,
	name	varchar(50) not null,
	category	varchar(50) not null,
	number	int,
	gender	varchar(20),
	pass	varchar(3000)
);

# テーブルemployeeへデータを入力
insert into employee(name, category, number, gender, pass)
	values('嫁阪雄大', '日配グロッサリー', 123209, 'male', '114514');
insert into employee(name, category, number, gender, pass)
	values('相田みつを', '青果', 123229, 'male', '1919810');
insert into employee(name, category, number, gender, pass)
	values('高弾力はじめ', 'レジ統合', 100000, 'female', '100081');
insert into employee(name, category, number, gender, pass)
	values('富士富雄', '管理', 000022, 'male', '1234');
insert into employee(name, category, number, gender, pass)
	values('大空スバル', 'レジ統合', 121212, 'female', '100081');




# テーブル cart の作成
drop table if exists cart; 
create table cart (	
	ident     int   auto_increment   primary   key,	
	quantity  int
);	