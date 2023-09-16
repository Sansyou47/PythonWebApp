# Flaskフレームワークを用いたWebアプリケーションの開発#2
## 1:概要
　今回の実習では、Pythonのフレームワークである**Flask**を用いたWebアプリケーションを作成しました。作成するアプリケーションはアルバイトや社員のシフトを管理するアプリケーションです。授業で学習済みのPHPではなく、わざわざ学習コストを割いてFlaskを使おうと思った理由についてですが、私自身が夏休みに参加したインターンシップにてFlaskを用いたWebアプリケーション開発を経験し、それが思いのほか楽しく学習としても非常に有益であったのと、インターン先の会社がPHPはもう全く使わないとう衝撃的なことを言われたためです。
## 2:今回行う予定の内容
　前回はデータベースとの連携が上手くいかなかったために、Flaskの勉強会のようなものができてしまった。今回はデータベースとの連携が上手くいったので、登録されている情報を参照、検索、また新規登録、削除、編集などの操作ができるように手を加えていく。
## 3:データベースの初期設定と環境変数
　データベースを使用するためには、初期設定の値を設定してあげないといけないのですが、例えばルートパスワードをそのまま記述してしまうとセキュリティを舐めた設計になってしまうので、今回は環境変数で渡す方式を採用しました。（それに関連してPythonコードでシステムの環境変数を取得できるか試したのがseisaku1ブランチの「環境変数を取得する！」機能。詳しくは参照してほしい。）具体的な流れは以下の通りです。    
"compose.yml"ファイルと同階層に".env"ファイルを設置→必要な変数を記述→"compsoe.yml"ファイルにはパスのみを記述→コンテナ起動時に自動で読み込まれる    
この方式を用いることで、安全性を確保しながら必要なデータをコンテナに渡すことができる。環境変数は必要があれば書き直したり追記してください。今回は利便性のために".env"ファイルも一緒にGitHub上に上げています
## 4:データベース
　本アプリではデータベースによるデータ管理を行っています。"MySQL"用のコンテナを同名で作成しているので詳しくはcompose.ymlファイルを参照してください。ここでは基本的なデータベースの情報を記しておきます。    
・データベース名：pytest  
・テーブル名：employee  
格納データ：  
| 項目名 | データ型 | 説明 | 補足 |
|:---|:---|:---|:---|
| 'ident' | int | **主キー** | 自動で追加(連番)、重複なし |
| 'name' | varchar(50) | 従業員の氏名 | |
| 'category' | varchar(50) | 配属部門 | |
| 'number' | int | 従業員番号 | 重複は基本的に無し |
| 'gender' | varchar | 性別データ | 時代の流れ的に削除の可能性あり |
| 'pass' | varchar(3000) | ログイン時に使用するパスワード | ハッシュ化して保存、デフォは"None" |    

　なお、テストデータとして6件のデータが既に登録されているので、詳細は"init.sql"ファイルを参照してください。コンテナをビルドする時にこのファイルが実行されてデータベースを初期化する仕組みであるので、初期データを何かしらの理由で変更する場合は適当なデータを記述してコンテナをリビルドしてください。  
'''
docker compsoe up --build
'''
上記コマンドはコンテナが停止状態の場合に有効であるため、コンテナが起動している場合は  
'''
docker compose down
'''
あるいは
'''
docker compose stop
'''
等のコマンドでコンテナを停止させてから最初のコマンドを実行してください。リビルドを行わないとデータベースを初期化することができないことを注意してください。  


## 最後に
　non-data,