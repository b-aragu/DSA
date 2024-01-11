# HASH TABLE
__Adv Constant time operation__
- An array with a hash function
- __Hash function__ - maps an arbitary size of data to an index in the hash function
- Hash function shd always :
	- produces same output
	- Should be first
	- Produce a random integer
- __collision__ - Two names map to the same location

__Creating A Hash table__
Lets define a struct to store the data
```c
typedef struct {
	char [MAX_SIZE];
	int age;
} person;

```
lets now create the hash table
```c
person *HASH_TABLE[TABLE_SIZE];
```
`TABLE_SIZE` represents the size of the hash table, now lets create a hash function to map each data to a position on the hash table.

```c
unsigned int hash(name)
{
	int length = strlen(name);
	unsigned int hash = 0;
	
	for (int i = 0; i < length; i++)
	{
		hash += hash * i + name[i] % TABLE_SIZE;
	}
	return (hash % 10) + 1; // make sure index is in the range 0 - 9 to fit hash table size
```

now lets create a function to insert data to the hash table
```c
bool hash_table_insert(person *p)
{
	if (p == NULL) return false;
	int index = hash(p->name);
	if(HASH_TABLE[index] != NULL)
	{
		printf("collision at index %d\n", index);
		return false;
	}
	HASH_TABLE[index] = p;
	return true;
}
```

now lets create a function to delete data in the hash table
```c
bool hash_table_delete(char *name)
{
	if (p == NULL) return false;
	int index = hash(p->name);
	if (HASH_TABLE[index] != NULL)
	{
		person *tmp = HASH_TABLE[index];
		HASH_TABLE[index] = NULL;
		return tmp
	}
	return NULL;
	
}
```
since we have created a function to insert and delete, lets create a function to print the hash table
```c
void hash_table_print()
{
	for (int i =0; i < TABLE_SIZE; i++)
		if (HASH_TABLE[i] != NULL)
		{
			printf("\t%d\t%s\n", i, HASH_TABLE[i]->name);
		}
		printf("\t%d\t---\n", i);
}
```

Now lets create a function to lookup for a name in the hash table
```c
person hash_table_lookup(char *name)
{
	int index = hash(name);
	if (HASH_TABLE[index] != NULL && strncmp(HASH_TABLE[index], name, MAX_SIZE)==0)
	{
		printf("%s found at index %d\n",name, index );
		return HASH_TABLE[index]
	}
	printf("%s not found ");
	return NULL;
}
```

Here is the full program

```c
/**
	hash_table.c
	A program to demonstrate hash table creation and its operation in C
 **/
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <stdbool.h>

 #define TABLE_SIZE 10
 #define MAX_SIZE 20

 // creating a struct person
 typedef struct {
	 char name[MAX_SIZE];
	 int age;
 }person;

 // creating the hashtable
 person *HASH_TABLE[TABLE_SIZE];

 // A hash function to insert value to hash table index
 unsigned int hash(name)
 {
	 unsigned int hash = 0;
	 int length = strnlen(name)
	 for (int i = 0; i < length; i++)
	 {
		 hash += hash * i + name[i] % TABLE_SIZE;
	 }
	 return (hash % TABLE_SIZE);
 }

 // function to insert data to the hash table
 bool hash_table_insert(person *p)
 {
	 if (p == NULL)
	 {
		 return false;
	 }
	 int index = hash(p->name);
	 if ( HASH_TABLE[index] != NULL)
	 {
		 printf(" cannot add ! There will be collision at index %d/n", index);
		 return false;
	 }
	 HASH_TABLE[index] = p;
	 return true;
 }
 // function to lookup
 person *hash_table_lookup(char *name)
 {
	 int index = hash(name);
	 if (HASH_TABLE[index] != NULL && strcmp(HASH_TABLE[index]->name, name, MAX_SIZE)==0)
	 {
		 printf("%s found at index %d", name, index);
		 return HASH_TABLE[index];
	 }
	 printf("%s not found\n", name);
	 return NULL;
	 
 }

// function to delete 
 bool hash_table_delete(char *name)
 {
	 int index = hash(name);
	 if (HASH_TABLE[index] != NULL)
	 {
		 person *tmp = HASH_TABLE[index];
		 HASH_TABLE[index] = NULL;
		 printf("deleted %s at index: %d", tmp->name, index);
		 return true;
	 }
	 printf("Error %s not found \n", name);
	 return false;
 }
// function to print 
void hash_table_print()
{
	for (int i = 0; i < TABLE_SIZE; i++)
	{
		(if HASH_TABLE[i] != NULL)
		{
			printf("\t%d\t%s\n", i, HASH_TABLE[i]->name);
		}
		printf("\t%d\t----\n", i);
	}
}

// entering the main function now
int main()
{
	person *p = &(person){"John", 20};
	person *baragu = &(person){"Baragu", 19};
	person *Hotensia = &(person){"Hotensia", 20};
	person *kamau = &(person){"kamau", 19};
	hash_table_insert(kamau);
	hash_table_print();
	hash_table_lookup("kamau");
	hash_table_insert(hotensia);
	hash_table_insert(baragu);
	hash_table_delete("Baragu")
	hash_table_lookup("Baragu")
	hash_table_print();

    return 0;
}
```
[hash_table.c](hash_table.c)

__Note:__ collision haven't still been addressed


