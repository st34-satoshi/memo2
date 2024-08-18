import { NextResponse } from 'next/server';
// import mysql from 'mysql2/promise';
// import { getConnection } from '@/app/dashboard/db';
import pool from '@/app/dashboard/db';

type Data = {
  id: number;
  menu_name: string;
  price: number;
  updated_datetime: Date;
  registered_datetime: Date;
};

export async function GET() {

  console.log('start get999999999')
  const sql = 'SELECT * FROM menu'
  try {
    // const connection = await getConnection();
    const db = await pool.getConnection()
    console.log('connection')
    // console.log(connection)
    console.log(db)
    // const [rows] = await connection.execute('SELECT * FROM menu');
    const [rows] = await db.execute('SELECT * FROM menu');
    // res.status(200).json(rows);
    console.log('API success!!!!!!!')
    return NextResponse.json(rows)
  } catch (error) {
    console.log('eeeeeeeeeee')
    return NextResponse.json({
      error: error
    }, { status: 500 })
    // res.status(500).json({ error: 'Database query failed' });
  }
  // return res
}