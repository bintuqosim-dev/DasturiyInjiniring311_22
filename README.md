class Graph {
    constructor(V) {
        this.V = V; // Grafikdagi tugunlar soni
        this.adj = new Array(V); // Har bir tugun uchun bo'sh ro'yhat yaratish
        for (let i = 0; i < V; i++) 
        this.adj[i] = []; // Har bir tugun uchun qo'shnilar ro'yxatini o'rnatish
    }
    
    addEdge(v, w) {
        this.adj[v].push(w); // v tuguniga w qo'shni tugunini qo'shish
    }

    DLS(src, target, limit) {
    if (src == target) return true; // Agar manba tugun maqsad tuguniga teng bo'lsa, topildi
    if (limit <= 0) return false; // Agar chuqurlik chegarasiga yetsak, qidirishni to'xtatamiz
    
    for (let i of this.adj[src].values()) {
        if (this.DLS(i, target, limit - 1) == true) 
        return true; // Qo'shnilarni chuqurlik chegarasi bilan rekursiv tekshirish
    }

    return false; // Maqsad topilmadi
}

IDDFS(src, target, max_depth) {
    for (let i = 0; i <= max_depth; i++) {
        if (this.DLS(src, target, i) == true) 
        return true; // Har bir chuqurlikda DLS chaqirish
    }
    return false; // Maqsad topilmadi
}}
g = new Graph(7);
g.addEdge(0, 1);
g.addEdge(0, 2);
g.addEdge(1, 3);
g.addEdge(1, 4);
g.addEdge(2, 5);
g.addEdge(2, 6);

let target = 6, maxDepth = 3, src = 0;
if (g.IDDFS(src, target, maxDepth) == true)
    document.write("Maqsadga maksimal chuqurlikdagi manbadan erishish mumkin");
else
    document.write("Maqsadga maksimal chuqurlikdagi manbadan yetib bo'lmaydi");


