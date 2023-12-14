import { useState } from "react";
import { postImage } from "./services/Evaluation";



const App = () => {

  const [file, setFile] = useState('');
  const [fileName, setFileName] = useState('');
  const [serverResponse, setServerResponse ] = useState('');
  const [previewImage, setPreviewImage] = useState(null);

  const encodeImageTo64 = (element) => {
    console.log(element)
    const targetFile = element.target.files[0];

    const reader = new FileReader();
    reader.onloadend = () => {
      console.log('Result:',  reader.result.split(',')[1]);
      const base64Data = reader.result.split(',')[1];
      setFile(base64Data);
      setFileName(targetFile.name);
      setPreviewImage(URL.createObjectURL(targetFile));
    }
    reader.readAsDataURL(targetFile);
  }
  const handleSubmit = async (event) => {
    event.preventDefault();
    
    const postBody = {
      file: file,
      fileName: fileName
    }
    console.log(postBody)
    const response = await postImage(postBody);
    console.log(response)
    setServerResponse(response.data.message)
  }
  
  return (
    <div className="App" >  
    <form onSubmit={handleSubmit}>
      <h4>
        Upload new file
      </h4>
      <input type="file" name="file" onChange={encodeImageTo64} ></input>
      <input type="submit" name="Upload"></input>
      <br></br>
      {previewImage && (
          <img
            src={previewImage}
            alt="Preview"
            style={{ maxWidth: '100%', maxHeight: '200px' }}
          />
        )}
        <br/  >
      <>{serverResponse}</>
    </form>
    </div>
  );
}

export default App;
