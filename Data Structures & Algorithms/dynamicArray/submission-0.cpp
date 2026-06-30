class DynamicArray {
private:
    int* data; //pointer to the array
    int size; //size of the array
    int capacity;

public:

    DynamicArray(int capacity) {
        size = 0;
        this->capacity = capacity;
        data = new int[capacity];
    }

    int get(int i) {
        return data[i];
    }

    void set(int i, int n) {
       data[i] = n;
    }

    void pushback(int n) {
        if (size == capacity){
            resize();
            data[size] = n;
                 size ++;
            }
            else{
                data[size] = n;
                 size ++;
            }
        
    }

    int popback() {
       int val = data[size - 1];
       size --;
       return val;
    }

    void resize() {
        //increment capacity
        capacity = capacity * 2;
        int *newData = new int[capacity];
        for (int i = 0; i < size; i++ ){
            newData[i] = data[i];
        }
        delete [] data;
        data = newData;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
