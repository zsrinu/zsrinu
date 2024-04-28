
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define a structure for Animal
struct Animal {
    char *name;
    int age;
    void (*makeSound)(void);
    void (*displayInfo)(struct Animal*);
};

// Define functions to simulate methods
void makeAnimalSound() {
    printf("The animal makes a sound\n");
}

void displayAnimalInfo(struct Animal *animal) {
    printf("Name: %s\n", animal->name);
    printf("Age: %d\n", animal->age);
}

// Constructor for Animal
struct Animal* createAnimal(char *name, int age) {
    struct Animal *animal = (struct Animal*)malloc(sizeof(struct Animal));
    animal->name = strdup(name);
    animal->age = age;
    animal->makeSound = makeAnimalSound;
    animal->displayInfo = displayAnimalInfo;
    return animal;
}

// Define a structure for Dog, inheriting Animal
struct Dog {
    struct Animal base;
};

// Constructor for Dog
struct Dog* createDog(char *name, int age) {
    struct Dog *dog = (struct Dog*)malloc(sizeof(struct Dog));
    dog->base = *createAnimal(name, age); // Initialize base Animal
    // Override methods
    dog->base.makeSound = (void (*)(void))printf("The dog barks\n");
    return dog;
}

// Main function
int main() {
    // Create an Animal object
    struct Animal *animal = createAnimal("Generic Animal", 5);

    // Create a Dog object
    struct Dog *dog = createDog("Buddy", 3);

    // Call methods
    animal->makeSound();
    animal->displayInfo(animal);

    dog->base.makeSound();
    dog->base.displayInfo((struct Animal*)dog);

    // Free memory
    free(animal->name);
    free(animal);
    free(dog->base.name);
    free(dog);

    return 0;
}

