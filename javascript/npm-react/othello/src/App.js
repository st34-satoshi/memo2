import './App.css';

function Board(){
  function cell(){
    const buttons = [];
    for (let i = 0; i < 8; i++) {
      buttons.push(
        <button>O</button>
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
      cell()
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
      </div>
    </>
  )
}

function App() {
  return (
    <div className="App">
      <Board />
    </div>
  );
}

export default App;
