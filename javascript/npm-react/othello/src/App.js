import './App.css';
import { useState } from 'react';

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

  function handleClick(s, t){
    const newCells = new Array(8);
    for(let i = 0; i < 8; i++) {
      newCells[i] = new Array(8).fill('・');
      for(let j = 0; j < 8; j++) {
        newCells[i][j] = cells[i][j];
      }
    }
    newCells[s][t] = 'A'
    setCells(newCells)
  }

  return (
    <div className="App">
      <Board cells={cells} handleClick={handleClick}/>
    </div>
  );
}

export default App;
