const startButton = document.querySelector('#startButton');
const stopButton = document.querySelector('#stopButton');

const recorder = new Recorder();

startButton.addEventListener('click', async function(){
    console.log('start recording');
    startRecording();
});

stopButton.addEventListener('click', async function(){
    console.log('stop recording');
    stopRecording();
});

function startRecording(){
    recorder.start();
}

function stopRecording(){
    // wav形式のblobを取得
    let audioBlob = recorder.stop();
    // 音声認識
    audioRecognize(audioBlob);
}

async function audioRecognize(audioBlob){
    const reader = new FileReader();
    reader.readAsDataURL(audioBlob);
  
    reader.onload = () => {
      const audioBase64 = reader.result.split(',')[1];
  
      // Speech-To-Textの設定値
      const data = {
        config: {
          encoding: "LINEAR16",
          languageCode: "ja-JP",
          audio_channel_count: 1
        },
        audio: {
          content: audioBase64
        }
      }
  
      fetch('https://speech.googleapis.com/v1/speech:recognize?key=' + API_KEY, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json; charset=utf-8'
        },
        body: JSON.stringify(data)
      }).then((response) => {
        if(!response.ok) {
          console.error('サーバーエラー');
        }
        return response.text();
      }).then((text) => {
        let result_json = JSON.parse(text);
        console.log(result_json);
        text = result_json.results[0].alternatives[0].transcript;
        console.log(text);
      }).catch((error)=>{
        console.error('通信に失敗しました', error);
      });
    };
  }