import mysql from 'mysql2/promise';

// export async function getConnection() {
//   const connection = await mysql.createConnection({
//     host: 'ec2-3-87-154-76.compute-1.amazonaws.com',  // データベースのホスト名
//     user: 'user1',  // MySQLのユーザー名
//     // password: 'if38%23kFG9R3 ',  // MySQLのパスワード
//     password: 'if38#kFG9R3 ',  // MySQLのパスワード
//     database: 'db_study1'  // 使用するデータベース
//   });
//   return connection;
// }

const pool = mysql.createPool({
    host: 'ec2-3-87-154-76.compute-1.amazonaws.com',  // データベースのホスト名
    user: 'user1',  // MySQLのユーザー名
    password: 'if38#kFG9R3',  // MySQLのパスワード
    // password: 'if38%23kFG9R3',  // MySQLのパスワード
    database: 'db_study1',  // 使用するデータベース
    waitForConnections: true
  // host: process.env.DB_HOST,
  // user: process.env.DB_USER,
  // password: process.env.DB_PASS,
  // database: process.env.DB_SCHEMA,
})

export default pool