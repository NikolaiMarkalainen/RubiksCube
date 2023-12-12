import { useState } from "react";
import { postImage } from "./services/Evaluation";



const App = () => {

  const [file, setFile] = useState('');
  const [fileName, setFileName] = useState('');

  const encodeImageTo64 = (element) => {
    console.log(element)
    const targetFile = element.target.files[0];

    const reader = new FileReader();
    reader.onloadend = () => {
      console.log('Result:',  reader.result.split(',')[1]);
      const base64Data = reader.result.split(',')[1];
      setFile(base64Data);
      setFileName(targetFile.name)
    }
    reader.readAsDataURL(targetFile);
  }
  const handleSubmit = (event) => {
    event.preventDefault();
    
    const postBody = {
      file: file,
      fileName: fileName
    }
    console.log(postBody)
    postImage(postBody);
  }
  
  return (
    <div className="App">  
    <form onSubmit={handleSubmit}>
      <h4>
        Upload new file
      </h4>
      <input type="file" name="file" onChange={encodeImageTo64}></input>
      <input type="submit" name="Upload"></input>
    </form>
    </div>
  );
}

export default App;
