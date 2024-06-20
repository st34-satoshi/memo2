import './App.css';
import { useState } from 'react';

function Board({cells}){
  function cell(i){
    const buttons = [];
    for (let j = 0; j < 8; j++) {
      buttons.push(
        <button className='gameCell'>{cells[i][j]}</button>
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
      {/* <div>
        <button>O</button>
        <button>X</button>
      </div>
      <div>
        <button>O</button>
        <button>X</button>
      </div> */}
      <div>
        {rows}
        {/* {cells} */}
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
  // for(let i = 0; i < 8; i++) {
  //   for(let j = 0; j < 8; i++) {
  console.log('hello')
  console.log(tmpCells)
  const [cells, setCells] = useState(tmpCells);

  return (
    <div className="App">
      <Board cells={cells}/>
    </div>
  );
}

export default App;
