/*
    Act 3.3 - Árbol Desplegado: Implementando un AVL Tree
    Autor: 
        * Brandon Josué Magaña Mendoza A01640162
    Programa que implementa un árbol de tipo AVL.
    Con sus métodos:
        * insert(int value)
        * del(int value)
        * find(int value)
        * print()
        * size()
*/

#include <bits/stdc++.h>

using namespace std;

template <class T>
class Node{ 
    /*Clase Nodo*/
    public:
        T data;
        int value;
        Node *left, *right;

        /*Constructor: Crea un nodo con sus valores de data 
                        y value inicializados
        Entrada:
                * T data: data de tipo template
                * int value: entero que representa su valor dentro del BST
        */
        Node(T data, int value){
            this->data = data;
            this->value = value;
            this->left = NULL;
            this->right = NULL;
        }

        //Constructor default
        Node(){
            this->data = NULL;
            this->value = 0;
            this->left = NULL;
            this->right = NULL;
        }
};

template <class T>
class AVLTree{
    public:
        /*Clase AVLTree*/
        Node<T> *root;

        //Constructor default
        AVLTree(){
            this->root = NULL;
        }

        /*
            Constructor:Crea un AVLTree con su raíz inicializada
            Entrada:
                * T data: data de tipo template
                * int value: entero que representa su valor dentro del BST
        */
        AVLTree(T data, int value){
            this->root = new Node<T>(data, value);
        }

        /*
            Método height, retorna la áltura de un Nodo
            Entrada:
                * Node<T>* root: Puntero de Nodo template
            Salida:
                * Altura del nodo
            Complejidad:
                * O(n) Lineal
        */
        int height(Node<T> *root){
            if (root == NULL) return 0;
            return max(height(root->left), height(root->right)) + 1;
        }

        /*
            Método getBalanceFactor, retorna el factor de balance de un nodo.
            Altura del lado Izquiero menos la altura del lado Derecho
            Entrada:
                * Node<T>* root: Puntero de Nodo template
            Salida:
                * Altura del nodo
            Complejidad:
                * O(n) Lineal
        */
        int getBalanceFactor(Node<T> *root){
            if (root == NULL) return 0;
            return height(root->left) - height(root->right);
        }

        /*
            Método rightRotate. Reordena los punteros de los nodos 
            haciendo una rotación a la derecha.
            Entrada:
                * Node<T>* y: Puntero de Nodo template
            Salida:
                * Node<T>* x: nuevo root de ese subárbol.
            Complejidad:
                O(1) Constante
        */
        Node<T> *rightRotate(Node<T> *y){
            //Lado izquierdo del nodo y
            Node<T> *x = y->left;
            //lado derecho del nodo x
            Node<T> *temp = x->right;

            //El lado derecho de x pasa a ser y
            x->right = y;

            //El lado izquierdo de y(anteriormente x),
            //pasa a ser el derecho(temp) de x
            y->left = temp;
            return x;
        }   

        /*
            Método leftRotate. Reordena los punteros de los nodos 
            haciendo una rotación a la izquierda.
            Entrada:
                * Node<T>* y: Puntero de Nodo template
            Salida:
                * Node<T>* x: nuevo root de ese subárbol.
            Complejidad:
                O(1) Constante
        */
        Node<T> *leftRotate(Node<T> *y){
            //Almacena en x el Lado derecho del nodo y
            Node<T> *x = y->right;
            //Almacena en temp lado izquierdo del nodo x
            Node<T> *temp = x->left;

            //El lado izquierdo de x pasa a ser y
            x->left = y;
            //El lado derecho de y(anteriormente x),
            //pasa a ser el derecho(temp) de x
            y->right = temp;
            return x;
        }

        /*
            Método balanceTree. Reordena los punteros de los nodos 
            haciendo la rotación correspondiente.
            Entrada:
                * Node<T>* root: Puntero de Nodo template
                * Node<T>* new_node: Puntero de Nodo template
            Salida:
                * Node<T>* : nuevo root de ese subárbol.
            Complejidad:
                O(1) Constante
        */
        Node<T> *balanceTree(Node<T> *root, Node<T> *new_node){
            //Se calcula el factor de balance
            //para determinar que rotación aplicar sobre el nodo.
            int balanceFactor = getBalanceFactor(root);

            //Caso Left Left
            if (balanceFactor > 1 && new_node->value < root->left->value)
                return rightRotate(root);

            //Caso Right Right
            if (balanceFactor < -1 && new_node->value > root->right->value)
            return leftRotate(root);

            //Caso Left Right
            if (balanceFactor > 1 && new_node->value > root->left->value){
                root->left = leftRotate(root->left);
                return rightRotate(root);
            }

            //Caso Right Left
            if (balanceFactor < -1 && new_node->value < root->right->value){
                root->right = rightRotate(root->right);
                return leftRotate(root);
            }

            //No necesita realizar rotaciones
            return root;
        }

        /*
            Método insert. Insera un nuevo nodo en el árbol y reordena los punteros de los nodos 
            haciendo las rotaciones correspondiente.
            Entrada:
                * Node<T>* root: Puntero de Nodo template
                * Node<T>* new_node: Puntero de Nodo template (nodo a insertar)
            Salida:
                * Node<T>* : nuevo root del árbol.
            Complejidad:
                * O(log n) logarítmica 
        */
        Node<T> *insert(Node<T> *root, Node<T> *new_node){
            //Si root no existe se genera e inserta el new_node
            if (root == NULL){
                return new_node;
            }
            //Si el valor del nodo a insertar es menor al valor de root actual
            //Llamada recursiva de método insert, aplicada sobre el
            //lado izquierdo de root
            if (new_node->value < root->value){
                root->left = insert(root->left, new_node);
            }
            //Si el valor del nodo a insertar es mayor o igual al valor de root actual
            //Llamada recursiva de método insert, aplicada sobre el
            //lado derecho de root
            else{
                root->right = insert(root->right, new_node);
            }

            //Se balancea el árbol haciendo las  rotaciones correspondientes
            //Se retorna el nodo
            root = balanceTree(root, new_node);

            //Retorno de nuevo root
            return root;
        }

        /*
            Método insert(void). Sobrecarga de funciones, crea el nodo 
            y manda a llamar a la función insert(Node<T>*, Node<T>*)
            Entrada:
                * T data: data de tipo template
                * int value: entero que representa su valor dentro del BST
            Salida: 
                N/A
            Complejidad:
                O(log n) logarítmica
        */
        void insert(T data, int value){
            Node<T> *new_node = new Node<T>(data, value);
            if (this->root != NULL){
                this->root = this->insert(this->root, new_node);
            }
            else{
                this->root = new_node;
            }
        }

        /*
            Método minValue. Obtiene el valor más pequeño de un subárbol.
            Entrada:
                * Node<T>* root: Puntero de Nodo template
            Salida:
                * Node<T>* root: Puntero a Nodo con el valor más pequeño
            Complejidad:
                * O(log n) Logaritmica, debido a que es un árbol AVL.

        */
        Node<T>* minValue(Node<T> *root){
            if (root != NULL){
                while (root->left != NULL)
                    root = root->left;
            }
            return root;
        }

        /*
            Método deleteNode. Elimina un nodo del árbol y lo balancea en caso
            de ser necesari, haciendo las rotaciones correspondientes
            Entrada:
                *  Node<T>* root: Puntero de Nodo template
                * int delete_value: entero que contiene el valor del nodo a borrar
            Salida:
                * Node<T>* : nuevo root del árbol.
            Complejidad:
                * O(log n) logaritmica 
        */
        Node<T> *deleteNode(Node<T> *root, int delete_value){
            //Encontrar el Nodo
            if (root == NULL)
                return root;

            if (delete_value < root->value){
                root->left = deleteNode(root->left, delete_value);
            }
            else if (delete_value > root->value){
                root->right = deleteNode(root->right, delete_value);
            }else{
                //Nodo con uno o ningún hijo
                
                //Nodo cuenta sin hijo izquierdo, regresa derecho
                if (root->left == NULL){
                    Node<T> *temp = root->right;
                    delete root;
                    return temp;
                }
                //Nodo cuenta sin hijo derecho, regresa izquierdo
                else if (root->right == NULL){
                    Node<T> *temp = root->left;
                    delete root;
                    return temp;
                }
                //Nodo cuenta con ambos hijos
                else{
                    //Encontramos el nodo de menor valor en el lado dercho.
                    Node<T> *temp = minValue(root->right);
                    //Asignamos su data y value al nodo root
                    root->data = temp->data;
                    root->value = temp->value;
                    //Eliminamos el nodo temp
                    root->right = deleteNode(root->right, temp->value);
                }
            }

            //Obtenemos balance Factor de root
            int balanceFactor = getBalanceFactor(root);
            
            // Caso Left Left 
            if (balanceFactor > 1 && getBalanceFactor(root->left) >= 0){
                return rightRotate(root);
            }

            // Caso Left Right 
            if (balanceFactor > 1 && getBalanceFactor(root->left) < 0){
                root->left = leftRotate(root->left);
                return rightRotate(root);
            }

            // Caso Right Right 
            if (balanceFactor < -1 && getBalanceFactor(root->right) <= 0){
                return leftRotate(root);
            }

            // Caso Right Left 
            if (balanceFactor < -1 && getBalanceFactor(root->right) > 0){
                root->right = rightRotate(root->right);
                return leftRotate(root);
            }
            // Retorno de nuevo root 
            return root;
        }

        /*
            Método del. Manda a llamar a la función deleteNode 
            y actualiza el nuevo root del árbol.
            
            Entrada:
                * int value: entero que contiene el valor del nodo a borrar
            Salida:
                * N/A
        */
        void del(int value){
            if(this->root != NULL){
                this->root=deleteNode(this->root,value);
            }
        }

        /*
            Método findValue. Se encarga de buscar un valor dentro 
            del árbol, regresa el nodo con el valor o un nodo nulo
            en caso de no encontrarlo.

            Entrada:
                *  Node<T>* root: Puntero de Nodo template
                *  int value: entero que contiene el valor del nodo a buscar
            Salida:
                * Node<T>* apuntador al nodo con el valor deseado o a nodo Nulo en
                caso de no encontrarse dentro del árbol.
            Complejidad:
                * O(log n) logarítmica
        */
        Node<T>* findValue(Node<T>* root, int value){
            if(root == NULL){
                return root;
            }
            if(value < root->value){
                root = findValue(root->left, value);
            }else if(value > root->value){
                root = findValue(root->right,value);
            }
            return root;
        }

        /*
            Método find. Se encarga de buscar un valor dentro 
            del árbol llamando a la función findValue, regresando true o false
            dependiendo en si el nodo fue encontrado.
            Entrada:
                *  int value: entero que contiene el valor del nodo a buscar
            Salida:
                * Node<T>* apuntador al nodo con el valor deseado o a nodo Nulo en
                caso de no encontrarse dentro del árbol.
            Complejidad:
                * O(log n) logarítmica
        */
        bool find(int value){
            Node<T>* result =findValue(this->root, value);

            return (result != NULL && result->value == value);
        }

        /*
            Método size(Node<T>*). retorna el número de nodos en el árbol.
            Entrada:
            *  Node<T>* root: Puntero de Nodo template
            Salida:
                Entero que representa el número de nodos en el árbol
            Complejidad:
                O(n) Lineal
        */
        int size(Node<T> *root){
            if (root == NULL)
                return 0;
            return 1 + size(root->left) + size(root->right);
        }

        /*
            Método size(). Sobrecarga de función size. Creada para ser utilizada en main.
            Llama a la función size(Node<T>*), recibiendo como parámetro el nodo root. 
            Entrada:
                * N/A
            Salida:
                * entero que representa el número de nodos del árbol
            Complejidad:
                O(n) Lineal
        */
        int size(){
            return size(this->root);
        }

        void print(){
            if(this->root == NULL) return;
            
            queue<Node<T>*> values;
            values.push(this->root);
            while(values.size() > 0){
                Node<T>* current= values.front();
                values.pop();
                
                cout<< current->data << " ";
                
                if(current->left != NULL){
                    values.push(current->left);
                }
                if(current->right != NULL){
                    values.push(current->right);
                }
            }
            cout<<endl;
        }

};

int main(){
    cout<<"\nCaso de prueba 1"<<endl;
    cout<<"-----------------"<<endl;
    AVLTree<string> mytree;
    mytree.insert("F", 9);
    mytree.insert("C", 5);
    mytree.insert("I", 10);
    mytree.insert("I", 0);
    mytree.insert("E", 6);
    mytree.insert("L", 11);
    mytree.insert("A", -1);
    mytree.insert("E", 1);
    mytree.insert("D", 2);
    mytree.insert("D", 12);
    mytree.insert("S", 15);

    cout<<"ESTADO ACTUAL DE ARBOL"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"| Test de busqueda |"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"10 se encuentra en el arbol?: "<<mytree.find(10)<<endl;
    cout<<"------------------"<<endl;
    cout<<"| Test de tamano |"<<endl;
    cout<<"------------------"<<endl;
    cout<<"Numero de nodos en el arbol : "<<mytree.size()<<endl;
    cout<<"---------------------------------"<<endl;
    cout<<"| Test de impresion(level order)|"<<endl;
    cout<<"---------------------------------"<<endl;
    mytree.print();
    
    mytree.del(10);
    cout<<"\nNodo con valor 10 Eliminado"<<endl;

    cout<<"\nESTADO ACTUAL DE ARBOL"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"| Test de busqueda |"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"10 se encuentra en el arbol?: "<<mytree.find(10)<<endl;
    cout<<"------------------"<<endl;
    cout<<"| Test de tamano |"<<endl;
    cout<<"------------------"<<endl;
    cout<<"Numero de nodos en el arbol : "<<mytree.size()<<endl;
    cout<<"---------------------------------"<<endl;
    cout<<"| Test de impresion(level order)|"<<endl;
    cout<<"---------------------------------"<<endl;
    mytree.print();

    cout<<"\nCaso de prueba 2"<<endl;
    cout<<"-----------------"<<endl;
    AVLTree<string> mytree2;
    mytree2.insert("H", 100);
    mytree2.insert("!", 19);
    mytree2.insert("L", 321);
    mytree2.insert("O", 1);
    mytree2.insert("A", -1);
    

    cout<<"ESTADO ACTUAL DE ARBOL"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"| Test de busqueda |"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"19 se encuentra en el arbol?: "<<mytree2.find(19)<<endl;
    cout<<"------------------"<<endl;
    cout<<"| Test de tamano |"<<endl;
    cout<<"------------------"<<endl;
    cout<<"Numero de nodos en el arbol : "<<mytree2.size()<<endl;
    cout<<"---------------------------------"<<endl;
    cout<<"| Test de impresion(level order)|"<<endl;
    cout<<"---------------------------------"<<endl;
    mytree2.print();
    
    mytree2.del(19);
    cout<<"\nNodo con valor 19 Eliminado"<<endl;

    cout<<"\nESTADO ACTUAL DE ARBOL"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"| Test de busqueda |"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"19 se encuentra en el arbol?: "<<mytree2.find(19)<<endl;
    cout<<"------------------"<<endl;
    cout<<"| Test de tamano |"<<endl;
    cout<<"------------------"<<endl;
    cout<<"Numero de nodos en el arbol : "<<mytree2.size()<<endl;
    cout<<"---------------------------------"<<endl;
    cout<<"| Test de impresion(level order)|"<<endl;
    cout<<"---------------------------------"<<endl;
    mytree2.print();

    cout<<"\nCaso de prueba 3"<<endl;
    cout<<"-----------------"<<endl;
    AVLTree<string> mytree3;
    mytree3.insert("R", 12);
    mytree3.insert("A", 4);
    mytree3.insert("O", 16);
    mytree3.insert("M", 8);
    mytree3.insert("U", 3);
    mytree3.insert("I", 0);
    mytree3.insert("B", 17);
    mytree3.insert("N", 5);
    mytree3.insert("S", 10);
    

    cout<<"ESTADO ACTUAL DE ARBOL"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"| Test de busqueda |"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"100 se encuentra en el arbol?: "<<mytree3.find(100)<<endl;
    cout<<"------------------"<<endl;
    cout<<"| Test de tamano |"<<endl;
    cout<<"------------------"<<endl;
    cout<<"Numero de nodos en el arbol : "<<mytree3.size()<<endl;
    cout<<"---------------------------------"<<endl;
    cout<<"| Test de impresion(level order)|"<<endl;
    cout<<"---------------------------------"<<endl;
    mytree3.print();
    
    mytree3.del(10);
    mytree3.del(3);
    mytree3.del(17);
    cout<<"\nNodo con valor 10 Eliminado"<<endl;
    cout<<"Nodo con valor 3 Eliminado"<<endl;
    cout<<"Nodo con valor 17 Eliminado"<<endl;

    cout<<"\nESTADO ACTUAL DE ARBOL"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"| Test de busqueda |"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"3 se encuentra en el arbol?: "<<mytree3.find(3)<<endl;
    cout<<"------------------"<<endl;
    cout<<"| Test de tamano |"<<endl;
    cout<<"------------------"<<endl;
    cout<<"Numero de nodos en el arbol : "<<mytree3.size()<<endl;
    cout<<"---------------------------------"<<endl;
    cout<<"| Test de impresion(level order)|"<<endl;
    cout<<"---------------------------------"<<endl;
    mytree3.print();

    cout<<"\nCaso de prueba 4"<<endl;
    cout<<"-----------------"<<endl;
    AVLTree<string> mytree4;
    mytree4.insert("R", 8);
    mytree4.insert("A", 5);
    mytree4.insert("M", 11);
    

    cout<<"ESTADO ACTUAL DE ARBOL"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"| Test de busqueda |"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"5 se encuentra en el arbol?: "<<mytree4.find(5)<<endl;
    cout<<"------------------"<<endl;
    cout<<"| Test de tamano |"<<endl;
    cout<<"------------------"<<endl;
    cout<<"Numero de nodos en el arbol : "<<mytree4.size()<<endl;
    cout<<"---------------------------------"<<endl;
    cout<<"| Test de impresion(level order)|"<<endl;
    cout<<"---------------------------------"<<endl;
    mytree4.print();
    
    mytree4.del(5);
    mytree4.del(8);
    mytree4.del(11);
    cout<<"\nNodo con valor 5 Eliminado"<<endl;
    cout<<"Nodo con valor 8 Eliminado"<<endl;
    cout<<"Nodo con valor 11 Eliminado"<<endl;

    cout<<"\nESTADO ACTUAL DE ARBOL"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"| Test de busqueda |"<<endl;
    cout<<"--------------------"<<endl;
    cout<<"3 se encuentra en el arbol?: "<<mytree4.find(3)<<endl;
    cout<<"------------------"<<endl;
    cout<<"| Test de tamano |"<<endl;
    cout<<"------------------"<<endl;
    cout<<"Numero de nodos en el arbol : "<<mytree4.size()<<endl;
    cout<<"---------------------------------"<<endl;
    cout<<"| Test de impresion(level order)|"<<endl;
    cout<<"---------------------------------"<<endl;
    mytree4.print();
    
    return 0;
}