#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define TABLE_SIZE 10
#define MAX_NAME 20

typedef struct {
  char name[MAX_NAME];
  int age;
  // other additions 
} person;

person *HASH_TABLE[TABLE_SIZE];

// Hash function we are using 
unsigned int hash(char *name)
{
  int length = strlen(name);
  unsigned int hash = 0;
  for (int i = 0; i < length; i++)
  {
    hash +=  hash *  i + name[i]  % TABLE_SIZE;
  }
  return (hash % 10) + 1;
}

// Inserting a person
bool hash_table_insert(person *p)
{

  if (p == NULL)  return false;
  int index  = hash(p->name);
  if (HASH_TABLE[index] != NULL)
  {
    printf("colision at index %d\n", index);
    return false;
  }
  HASH_TABLE[index] = p;
  return true;
}

// Function to find a person
person *hash_table_lookup(char *name)
{
  int index = hash(name);
  if (HASH_TABLE[index] != NULL && strncmp(HASH_TABLE[index]->name, name, MAX_NAME) == 0)
  {
    printf("Found %s at index %d\n", name, index);
    return HASH_TABLE[index];
  }
  return NULL;
}

// delete a person
person *hash_table_delete(char *name)
{
  int index = hash(name);
  if (HASH_TABLE[index] != NULL && strncmp(HASH_TABLE[index]->name, name, MAX_NAME)==0)
  {
    person *tmp = HASH_TABLE[index];
    printf("Deleted %s at index %d\n", name, index);
    HASH_TABLE[index] = NULL;
    return tmp;
  }
  return NULL;
}

// function to print the hash table
void hash_table_print()
{
  for (int i = 0; i < 10; i++)
  {
    if (HASH_TABLE[i] != NULL)
    {
      printf("\t%d\t%s\n", i, HASH_TABLE[i]->name);
    }
    else {
        printf("\t%i\t---\n", i);
    }
  }
}

// Main function
int main(){
  
  person *p = &(person){"John", 20};
  person  *John = &(person){"JOHN", 54};
  person *bara = &(person){"Baragu", 19};
  
  hash_table_insert(John);
  hash_table_insert(p);
  hash_table_insert(bara);
  hash_table_lookup("John");
  hash_table_print();
  hash_table_delete("John");
  hash_table_lookup("John");
  hash_table_print();
  

  return 0;
}
