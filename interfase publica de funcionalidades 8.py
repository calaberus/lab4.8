class ListDeTareas:

    def __init__(self):
       self.tareas=[]  
           
        
    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)
        print(f"tarea´{tarea}´agrgar a la lista.")
        
    def eliminar_tarea(self,tarea):
         if tarea in self.tareas:
             self.tareas.remove(tareas)
             print(f"tarea´{tarea}´eliminada de la lista.")
         else:
             print(f"tarea´{tarea}´no encontrada.")
                  
          
    def mostar_tarea(self):
         if self.tareas:
             print("tareas pendientes:",",".join(self.tareas)) 
            
         else:
             print("no hay tareas pendientes.")
             
             
             
             
             
          
             
             
       
            
    
            
            
        