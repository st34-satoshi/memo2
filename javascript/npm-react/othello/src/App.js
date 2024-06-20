import './App.css';
import { useState } from 'react';

/**
 * 反転する[i, j]の配列を返す
 * @param {*} cells 
 * @param {*} i 
 * @param {*} j 
 */
function flipCells(cells, i, j){
  const directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
  ]
  return [[4,4]]
}

/**
 * 現在のcellsから変更した後のcellsを返す
 * @param {*} cells 
 * @param {*} p 駒
 */
function updatedCells(cells, fCells, p){
  for (let i = 0; i < fCells.length; i++) {
    const u = fCells[i]
    cells[u[0]][u[1]] = p
  }

  return cells
}

function Board({cells, handleClick}){
  function cell(i){
    const buttons = [];
    for (let j = 0; j < 8; j++) {
      buttons.push(
        <button className='gameCell' onClick={() => handleClick(i, j)}>{cells[i][j]}</button>
      )
    }
    return(
      <div>
        {buttons}
      </div>
    )
  }
  const rows = [];
  for (let i = 0; i < 8; i++) {
    rows.push(
      cell(i)
    )
  }

  return(
    <>
      <div>
        {rows}
      </div>
    </>
  )
}

function App() {
  const tmpCells = new Array(8);
  for(let i = 0; i < 8; i++) {
    tmpCells[i] = new Array(8).fill('・');
  }
  tmpCells[3][3] = '⚪️'
  tmpCells[3][4] = '⚫️'
  tmpCells[4][4] = '⚪️'
  tmpCells[4][3] = '⚫️'
  const [cells, setCells] = useState(tmpCells);
  const [nextP, setNextP] = useState('⚫️')

  function nextPiece(){
    if(nextP === '⚫️'){
      return '⚪️';
    }
    return '⚫️';
  }

  function handleClick(s, t){
    const newCells = new Array(8);
    for(let i = 0; i < 8; i++) {
      newCells[i] = new Array(8).fill('・');
      for(let j = 0; j < 8; j++) {
        newCells[i][j] = cells[i][j];
      }
    }
    // TODO: 盤面を変更できるか調べる
    const fCells = flipCells(newCells, s, t, nextP)
    console.log(fCells)
    // TODO: からなら何もしない, 要素があれば更新する
    if(fCells.length === 0){
      console.log('no flip')
      return;
    }
    newCells[s][t] = nextP
    setNextP(nextPiece())
    setCells(updatedCells(newCells, fCells, nextP))
  }

  return (
    <div className="App">
      <Board cells={cells} handleClick={handleClick}/>
    </div>
  );
}

export default App;
