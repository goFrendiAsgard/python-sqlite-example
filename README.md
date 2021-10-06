# SQLite dasar

* Install sqlite
* Coba-coba kalimat sql [di sini](https://sqlite.org/cli.html)

```sh
sqlite3 database.db
```

Bikin tabel, insert, dan select 

```sql
create table book(title varchar(30), author varchar(30));
insert into book(title, author) values('doraemon', 'fujiko f. fujio');
insert into book(title, author) values('one piece', 'eichiro oda');
select * from book;
-- doraemon|fujiko f. fujio
-- one piece|eichiro oda
```

Untuk update/delete:

```sql
update book set author='dono' where title='doraemon';
delete from book where author='dono';
```

# Jalankan SQL dari Python

```sh
pip install sqlite3
```

