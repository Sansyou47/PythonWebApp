# Flaskフレームワークを用いたWebアプリケーションの開発#2
## 1:概要
　今回の実習では、Pythonのフレームワークである**Flask**を用いたWebアプリケーションを作成しました。作成するアプリケーションはアルバイトや社員のシフトを管理するアプリケーションです。授業で学習済みのPHPではなく、わざわざ学習コストを割いてFlaskを使おうと思った理由についてですが、私自身が夏休みに参加したインターンシップにてFlaskを用いたWebアプリケーション開発を経験し、それが思いのほか楽しく学習としても非常に有益であったのと、インターン先の会社がPHPはもう全く使わないとう衝撃的なことを言われたためです。
## 2:今回行う予定の内容
　前回はデータベースとの連携が上手くいかなかったために、Flaskの勉強会のようなものができてしまいました。今回はデータベースとの連携が上手くいったので、登録されている情報を参照、検索、また新規登録、削除、編集などの操作ができるように手を加えていきます。
## 3:Dockerコンテナの構成変更
　今回はデータベースをメインで使用していくため、少しコンテナの構成を変更しています。主な変更点として、Pythonを実行するコンテナのベースイメージを"python:alpine"から"python:3.8"に変更しています。また、RUN命令による"pip install"コマンドでインストールしている内容を大きく変更しています。インストールしているパッケージは"requirements.txt"で確認してください。細かな変更を加えているため、前回のコンテナ構成では今回のスクリプトが動作しない点を注意してください。
## 4:データベースの初期設定と環境変数
　データベースを使用するためには、初期設定の値を設定してあげないといけないのですが、例えばルートパスワードをそのまま記述してしまうとセキュリティを舐めた設計になってしまうので、今回は環境変数で渡す方式を採用しました。（それに関連してPythonコードでシステムの環境変数を取得できるか試したのがseisaku1ブランチの「環境変数を取得する！」機能。詳しくは参照してほしい。）具体的な流れは以下の通りです。    
"compose.yml"ファイルと同階層に".env"ファイルを設置→必要な変数を記述→"compsoe.yml"ファイルにはパスのみを記述→コンテナ起動時に自動で読み込まれる    
この方式を用いることで、安全性を確保しながら必要なデータをコンテナに渡すことができる。環境変数は必要があれば書き直したり追記してください。今回は利便性のために".env"ファイルも一緒にGitHub上に上げています
## 5:データベース
　本アプリではデータベースによるデータ管理を行っています。"MySQL"用のコンテナを同名で作成しているので詳しくはcompose.ymlファイルを参照してください。ここでは基本的なデータベースの情報を記しておきます。    
### データベース名：pytest  
### テーブル名：employee  
雇用されている従業員のデータを格納しているテーブルです。各従業員の配属や雇用形態と契約時間など。  
### 格納データ：  
| 項目名 | データ型 | 説明 | 補足 |
|:---|:---|:---|:---|
| ident | int | **主キー** | 自動で追加(連番)、重複なし |
| name | varchar(50) | 従業員の氏名 | |
| category | varchar(50) | 配属部門 | |
| auth | int | 管理画面に入る権限 | 0：全権限保持、1：一部権限保持、2：一般ユーザー |
| number | int | 従業員番号 | 重複は基本的に無し |
| gender | varchar | 性別データ | 時代の流れ的に削除の可能性あり |
| start | int | 始業時刻 | 24時間表記、15分刻み |
| finish | int | 終業時刻 | 24時間表記、15分刻み |
| pass | varchar(3000) | ログイン時に使用するパスワード | ハッシュ化して保存、デフォは"None" |    


　なお、"employee"テーブルにはテストデータとして6件のデータが既に登録されているので、詳細は"init.sql"ファイルを参照してください。コンテナをビルドする時にこのファイルが実行されてデータベースを初期化する仕組みであるので、初期データを何かしらの理由で変更する場合は適当なデータを記述してコンテナをリビルドしてください。リビルドを行わないとデータベースを初期化することができないことに注意してください。  
## 6:データのハッシュ化
　前項目にて、パスワードデータをハッシュ化してデータベースへ格納していると説明しました。これについてですが、一般的にデータベースへパスワードデータを格納する場合、平文で
格納するのは非常にリスクがあります。万が一漏洩してしまった場合、平文だと攻撃者が入手したデータをそのまま利用できてしまうため、ハッシュ化して本来のデータがわからないようにする必要があります。  
　今回のアプリではアルゴリズムに"SHA-256"を採用しています。データの受け渡しから暗号化までのプロセスは、まずフォームに利用者が設定したいパスワードを入力します。入力されたデータは"POST"メソッドでPythonスクリプトへ渡されます。Pythonスクリプトでは渡されたデータを標準ライブラリの"hashlib"でハッシュ値に変換処理を行い、データベースへ受け渡しを行います。  
　フォームからPOSTメソッドで送信されたデータはPythonスクリプトの"request.form.get"によってデータの受け取りを実現しています。ここで注意してほしいのが、"request.form.get"ではデフォルトの値が"None"になることです。例えば、パスワードを設定したくないユーザーがパスワード入力欄を空白で送信した場合、Pythonスクリプトでは何も送信されてこないため、デフォルトの値が設定されてしまいます。つまり、文字列"None"がハッシュ化された値がそのユーザーのパスワードとして設定されてしまいます。この問題点については、当初では"request.form"を使用することでデフォルトの値を使用しないことで解決しようと思っていましたが、この場合送信されたデータが空の場合、Pythonスクリプトでは空検知ができずにクライアントのブラウザにステータスコード400番のエラーを吐いてしまいます。フォームが空の場合の処理を実装したかったので今回はデフォルトが"None"になるようにしています。
## 最後に
　non-data,