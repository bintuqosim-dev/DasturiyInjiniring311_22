// Ikkilik daraxt tuzilmasidan foydalangan holda Massivdagi unikal qiymatlarni saralash

class TreeNode {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  function addToTree(root, value) {
    if (root === null) return new TreeNode(value);
  
    if (value < root.value) {
      root.left = addToTree(root.left, value);
    } else if (value > root.value) {
      root.right = addToTree(root.right, value);
    }
  
    return root;
  }
  
  function inOrderTraversal(root, result = []) {
    if (root === null) return result;
  
    inOrderTraversal(root.left, result);
    result.push(root.value);
    inOrderTraversal(root.right, result);
  
    return result;
  }
  
  function uniqueSortArray(arr) {
    let root = null;
  
    for (const value of arr) {
      root = addToTree(root, value);
    }

    return inOrderTraversal(root);
  }
  
  // Namuna uchun
  const array = [5, 3, 8, 3, 5, 7, 8, 1];
  const sortedUniqueArray = uniqueSortArray(array);
  
  console.log("Saralangan unikal qiymatlar:", sortedUniqueArray);
  