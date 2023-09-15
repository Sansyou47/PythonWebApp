
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
	values('嫁阪雄大', '日配グロッサリー', 123209, 'male', 'None');
insert into employee(name, category, number, gender, pass)
	values('相田みつを', '青果', 123229, 'male', 'None');
insert into employee(name, category, number, gender, pass)
	values('高弾力はじめ', 'レジ統合', 100000, 'female', 'None');
insert into employee(name, category, number, gender, pass)
	values('富士富雄', '管理', 000022, 'male', 'None');
insert into employee(name, category, number, gender, pass)
	values('大空スバル', 'レジ統合', 121212, 'female', 'None');
insert into employee(name, category, number, gender, pass)
	values('岸辺露伴', '書籍', 123210, 'male', 'ecb666d778725ec97307044d642bf4d160aabb76f56c0069c71ea25b1e926825');

