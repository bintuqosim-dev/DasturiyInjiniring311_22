/* Graph Data Structure
Mavzu: Iterativ chuqurlashtiruvchi qidiruv (IDS) yoki iterativ chuqurlashtiruvchi birinchi qidiruv (IDDFS)
*/
/* Maqsadli tugunga kirish mumkin yoki yo'qligini qidirish uchun Javascript dasturi
berilgan maksimal chuqurlikka ega manba.*/

      // Grafik klassi qo'shnilik yordamida yo'naltirilgan grafikni ifodalaydi
      // ro'yxat ko'rinishi.
      console.log();
      class Graph{
          constructor(V){
              this.V = V;
              this.adj = new Array(V);
              for(let i = 0; i < V; i++)
                  this.adj[i] = [];
          }

          addEdge(v, w){
              this.adj[v].push(w); // Add w to v’s list.
          }

          /* Chuqurlik bilan cheklangan qidiruvni amalga oshirish funksiyasi berilgan "src" manbasidan */
          DLS(src, target, limit){
              if (src == target)
                  return true;

              // Agar maksimal chuqurlikka erishilsa, takrorlashni to'xtating.
              if (limit <= 0)
                  return false;

              // Manba cho'qqisiga ulashgan barcha cho'qqilar uchun takrorlang
              for (let i of this.adj[src].values()){
                  if (this.DLS(i, target, limit-1) == true)
                      return true;
              }

              return false;
          }

          /* IDDFS dan nishonga erishish mumkinmi yoki yoʻqligini izlash uchun rekursiv DFSUtil() dan foydalanadi.*/
          IDDFS(src, target, max_chuqurlik){
          
              /* Maksimal chuqurlikka qadar qidiruvni qayta-qayta cheklang.*/
              for (let i = 0; i <= max_chuqurlik; i++){
                  if (this.DLS(src, target, i) == true)
                      return true;
              }

              return false;
          }
      }
      // Driver code

      // Keling, 7 ta tugunli yo'naltirilgan grafik yarataylik
      g = new Graph(7);
      g.addEdge(0, 1);
      g.addEdge(0, 2);
      g.addEdge(1, 3);
      g.addEdge(1, 4);
      g.addEdge(2, 5);
      g.addEdge(2, 6);

      let target = 6, maxChuqurlik = 3, src = 0;
      if (g.IDDFS(src, target, maxChuqurlik) == true)
          document.write("Maqsadga maksimal chuqurlikdagi manbadan erishish mumkin");
      else
          document.write("Maqsadga maksimal chuqurlikdagi manbadan yetib bo'lmaydi");
          
       
