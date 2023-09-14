use pytest

# テーブル items の作成
drop table if exists items; 
# テーブルitemsの作成
create table items(
	ident	int auto_increment primary key,
	name	varchar(50) not null,
	category	varchar(50) not null,
	number	int,
	gender	varchar(20),
	pass	varchar(10)
);

# テーブルitemsへデータを入力
insert into items(name, category, number, gender, pass)
	values('嫁阪雄大', '日配グロッサリー', 123209, 'male', '114514');
insert into items(name, category, number, gender, pass)
	values('相田みつを', '青果', 123229, 'male', '1919810');
insert into items(name, category, number, gender, pass)
	values('高弾力はじめ', 'レジ統合', 100000, 'female', '100081');




# テーブル cart の作成
drop table if exists cart; 
create table cart (	
	ident     int   auto_increment   primary   key,	
	quantity  int
);	