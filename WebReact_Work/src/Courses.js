import { useEffect, useImperativeHandle, useState } from "react";

const Item = (i,editItem) =>{
    const [edit,setEdit] = useState(false);
    const [name,setName] = useState("");
    const [cost,setCost] = useState(0);
    const [quantity,setQuantity] = useState(0);
    if (edit){
        return <>
        <input type="text" value={name}></input>
        <input type="decimal" value={cost}></input>
        <input type="number" value={quantity}></input>
        <button onClick={editItem}>Edit</button>
        </>;
    }
    return <>
    <p>{name}   {cost}  {quantity}  
    <button onClick={editItem}>Edit</button></p>
    </>;
};

const ItemsList = ({items,removeItem,editItem}) => {
  return items.map((i, idx)=> <>
  <p>{i}<button onClick={() => {removeItem(idx)}}>Remove</button></p></>);
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
  const [items,setItems] = useState([]);
  const addItem = (v) => {setItems(items.concat(<Item />))};
  const removeItem = (idx) => {
    setItems(items.filter((i,id)=>id!=idx));
  };
  const editItem = (idx,i) => {
    items[idx] = i; setItems(items);
  };
  return <div>
    <AddItemForm addItem={addItem}/>
    <ItemsList items={items} removeItem={removeItem} editItem={editItem}/>
  </div>;
}
 
export default ItemsApp;
 