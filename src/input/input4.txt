/* 
    Act 3.2 - Árbol Heap
    Brandon Josué Magaña Mendoza A01640162

    Implementación de Binary Search Tree de tipo Max Heap de Enteros.

    Con Métodos:
        -push
        -pop
        -top
        -empty
        -size
*/

#include <bits/stdc++.h>
using namespace std;

class MaxHeap { 
        public:
            //Atributos
            vector<int> maxHeap; // vector que almacena el heap ordenado
            int len; // tamaño del heap
            
            //Constructor
            MaxHeap(){
                this->len=0;
            }

            //Deconstructor
            ~MaxHeap(){

            }

            // Métodos Principales

            // Función que ingresa un nodo al heap, llama a la función heapifyUp y aumenta el tamaño del vector
            // Complejidad: 
            void push(int item) {
                maxHeap.push_back(item);
                len++;
                heapifyUp();
            }

            // Función que elimina la raíz del heap, llama a la función heapifyDown y disminuye el tamaño del vector
            // Complejidad: O(Log(n))
            void pop(){
                if(len==0) return;
                maxHeap[0]= maxHeap[len-1];
                heapifyDown();
                len--;
                maxHeap.erase(maxHeap.begin()+(len));
                return;
            }
            
            // Función que retorna el nodo raíz
            // Complejidad: O(1)
            int top(){
                if(len == 0) return -1;
                return maxHeap[0];
            }

            // Función que indica si el heap está vacío
            // Complejidad: O(1)		
            bool empty(){
                return len == 0;
            }

            // Función que retorna el tamaño del heap
            // Complejidad: O(1)
            int size(){
                return len;
            }

            //Función que imprime por pantalla los valores dentro del MaxHeap
            void print(){
                for(auto &it: maxHeap){
                    cout << it << endl;
                }
                cout<<"\n";
            }  
            
        private:
		    // Función auxiliar que intercambia dos nodos
		    // Complejidad: O(1)
            void swap(int i1, int i2){
                int temp = maxHeap[i1];
                maxHeap[i1] = maxHeap[i2];
                maxHeap[i2] = temp;
            }
        
            // Funciones que indican la existencia de nodo izquierdo, derecho o padre
            // Complejidad: O(1)
            bool hasRight(int index){
                return getRightIndex(index)< this->maxHeap.size();
            }
		
            bool hasLeft(int index) {
                return getLeftIndex(index) < this->maxHeap.size();
            }
            
            bool hasParent(int index){
                return getParentIndex(index) >= 0;
            }

            // Getters de los índices de nodo padre, izquierdo y derecho
            // Complejidad: O(1)
            int getParentIndex(int index){return (index-1)/2;}
            
            int getLeftIndex(int index){return index*2 + 1;}

            int getRightIndex(int index){return index*2 + 2;}

            // Getters de nodos padre, izquierdo y derecho
            // Complejidad: O(1)
            int getRight(int index){
                return maxHeap[getRightIndex(index)];
            }

            int getLeft(int index){
                return maxHeap[getLeftIndex(index)];
            }

            int getParent(int index){
                return maxHeap[getParentIndex(index)];
            }

            //Función encargada de hacer los intercambios en el array desde el ultimo elemento hasta el primero
            //Complejidad: O(log n)
            void heapifyUp(){
                int current = len - 1; 
                while(hasParent(current) && getParent(current) < maxHeap[current]){
                    swap(current, getParentIndex(current)); 
                    current = getParentIndex(current);
                }
            }
            
            //Función encargada de hacer los intercambios en el array desde el primer elemento hasta el último
            //Complejidad: O(log n)
            void heapifyDown(){
                int index = 0;
                while(hasLeft(index)){
                    int maxChildIndex = getLeftIndex(index);
                    if(hasRight(index) && getRight(index) > getLeft(index)){
                        maxChildIndex = getRightIndex(index);
                    }
                    if(maxHeap[maxChildIndex] > maxHeap[index]){
                        swap(maxChildIndex, index);
                    }else{
                        break;
                    }
                    index = maxChildIndex;
                }
            }    
};

int main() {
    //Declaración de MaxHeap de prueba
    MaxHeap heap1 = MaxHeap();
    MaxHeap heap2= MaxHeap();
    MaxHeap heap3= MaxHeap(); 
    MaxHeap heap4= MaxHeap();
    
    cout<<"-------------------"<<endl;  
    cout<<"Caso de prueba 1"<<endl;
    cout<<"-------------------"<<endl;
    
    //Agregando datos al Heap
    heap1.push(1);
    heap1.push(2);
    heap1.push(3);
    heap1.push(4);
    heap1.push(5); 
    heap1.push(6); 
    heap1.push(7); 

    //Impresión estado actual de Max Heap
    cout<<"Estado actual de Max Heap:"<<endl;
    cout<<"Top: "<<heap1.top()<<endl; 
    cout <<"Tamano: "<< heap1.size()<<endl;
    cout<<"Empty: "<<heap1.empty()<<endl;
    cout<<"Heap: "<<endl;
    heap1.print();

    //Removiendo el elemento con mayor prioridad
    heap1.pop();

    //Impresión estado actual de Max Heap
    cout<<"Estado actual de Max Heap:"<<endl;
    cout<<"Top: "<<heap1.top()<<endl; 
    cout <<"Tamano: "<< heap1.size()<<endl;
    cout<<"Empty: "<<heap1.empty()<<endl;
    cout<<"Heap: "<<endl;
    heap1.print();

    cout<<"-------------------"<<endl;  
    cout<<"Caso de prueba 2"<<endl;
    cout<<"-------------------"<<endl;
    
    //Agregando datos al Heap
    heap2.push(56);
    heap2.push(75);
    heap2.push(20);
    heap2.push(15); 
    heap2.push(432); 
    heap2.push(32); 

    //Impresión estado actual de Max Heap
    cout<<"Estado actual de Max Heap:"<<endl;
    cout<<"Top: "<<heap2.top()<<endl; 
    cout <<"Tamano: "<< heap2.size()<<endl;
    cout<<"Empty: "<<heap2.empty()<<endl;
    cout<<"Heap: "<<endl;
    heap2.print();

    //Removiendo el elemento con mayor prioridad 3 veces
    heap2.pop();
    heap2.pop();
    heap2.pop();

    //Impresión estado actual de Max Heap
    cout<<"Estado actual de Max Heap:"<<endl;
    cout<<"Top: "<<heap2.top()<<endl; 
    cout <<"Tamano: "<< heap2.size()<<endl;
    cout<<"Empty: "<<heap2.empty()<<endl;
    cout<<"Heap: "<<endl;
    heap2.print();

    cout<<"-------------------"<<endl;  
    cout<<"Caso de prueba 3"<<endl;
    cout<<"-------------------"<<endl;
    

    //Impresión estado actual de Max Heap
    cout<<"Estado actual de Max Heap:"<<endl;
    cout<<"Top: "<<heap3.top()<<endl; 
    cout <<"Tamano: "<< heap3.size()<<endl;
    cout<<"Empty: "<<heap3.empty()<<endl;
    cout<<"Heap: "<<endl;
    heap3.print();

    //Removiendo el elemento con mayor prioridad 3 veces
    heap3.pop();
    
    //Agregando datos al Heap
    heap3.push(10);
    heap3.push(30);
    heap3.push(20);

    //Impresión estado actual de Max Heap
    cout<<"Estado actual de Max Heap:"<<endl;
    cout<<"Top: "<<heap3.top()<<endl; 
    cout <<"Tamano: "<< heap3.size()<<endl;
    cout<<"Empty: "<<heap3.empty()<<endl;
    cout<<"Heap: "<<endl;
    heap3.print();

    cout<<"-------------------"<<endl;  
    cout<<"Caso de prueba 4"<<endl;
    cout<<"-------------------"<<endl;
    
    //Agregando datos al Heap
    heap4.push(46);
    heap4.push(32);
    heap4.push(91);
    heap4.push(64);
    heap4.push(23);
    heap4.push(19);

    //Impresión estado actual de Max Heap
    cout<<"Estado actual de Max Heap:"<<endl;
    cout<<"Top: "<<heap4.top()<<endl; 
    cout <<"Tamano: "<< heap4.size()<<endl;
    cout<<"Empty: "<<heap4.empty()<<endl;
    cout<<"Heap: "<<endl;
    heap4.print();

    //Removiendo el elemento con mayor prioridad 3 veces
    heap4.pop();
    heap4.pop();
    heap4.pop();
    heap4.pop();
    heap4.pop();
    heap4.pop();

    //Impresión estado actual de Max Heap
    cout<<"Estado actual de Max Heap:"<<endl;
    cout<<"Top: "<<heap4.top()<<endl; 
    cout <<"Tamano: "<< heap4.size()<<endl;
    cout<<"Empty: "<<heap4.empty()<<endl;
    cout<<"Heap: "<<endl;
    heap4.print();

    return 0;
}