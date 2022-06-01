import { useEffect, useImperativeHandle, useState } from "react";
 
const ItemsList = ({items,removeItem}) => {
  return items.map((i, idx)=><>
  <p>{i}
  <button onClick={() => {removeItem(idx)}}>Remove</button>
  </p></>);
}
 
const AddItemForm = ({addItem}) => {
  const [currentText, setCurrentText] = useState("");
  const handleAdd = () => {addItem(currentText)};
  const handleChange = e => {setCurrentText(e.target.value)};
  return <>
    <input type="text" onChange={handleChange} value={currentText}></input>
    <button onClick={handleAdd} type="submit">Validation</button>
  </>
};

const ItemsApp = () => {
  const [items,setItems] = useState(["test"]);
  const addItem = (v) => {setItems(items.concat(v))};
  const removeItem = (idx) => {
    setItems(items.filter((i,id)=>id!=idx));
  };
  return <div>
    <AddItemForm addItem={addItem}/>
    <ItemsList items={items} removeItem={removeItem}/>
  </div>;
}
 
export default ItemsApp;
 