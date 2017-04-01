#include <stdlib.h>
#include <stdio.h>	
typedef struct Node
{
    int data;
    struct Node* next;
}Node;


Node* insert(Node *head,int data)
{
	// Aloca o valor primeiro 
	Node *x = malloc(sizeof(Node));
	x->data = data;
	x->next = NULL;

    if(head == NULL){
    	// printf("to no head\n");
    	return x;
    } else {
    	Node *aux = NULL;
    	Node *prev = NULL;
    	for(aux = head; aux != NULL; aux = aux->next){
    		// printf("qual valor ta aqui dentro %d\n", aux->data);
    		prev = aux;
    	}
    	// printf("To aqui\n");

    	prev->next = x;
		// printf("To aqu2i\n");    	
    	return head;
    }
}

void display(Node *head)
{
	Node *start=head;
	while(start)
	{
		printf("%d ",start->data);
		start=start->next;
	}
}
int main()
{
	int T,data;
    scanf("%d",&T);
    Node *head=NULL;	
    while(T-->0){
        scanf("%d",&data);
        head=insert(head,data);
    }
  display(head);
		
}