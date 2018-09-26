//Code taken from the internet
#include "pch.h"
#include <stdio.h> 
#include <stdlib.h> 

struct node
{
	int data;
	struct node* leftNode, *rightNode;
};

struct node *lca(struct node* root, int num1, int num2)
{
	if (root == NULL) return NULL;

	if (root->data > num1 && root->data > num2)
		return lca(root->leftNode, num1, num2);

	if (root->data < num1 && root->data < num2)
		return lca(root->rightNode, num1, num2);

	return root;
}

struct node* newNode(int data)
{
	struct node* node = (struct node*)malloc(sizeof(struct node));
	node->data = data;
	node->leftNode = node->rightNode = NULL;
	return(node);
}

int main()
{
	struct node *root = newNode(20);
	root->leftNode = newNode(8);
	root->rightNode = newNode(22);
	root->leftNode->leftNode = newNode(4);
	root->leftNode->rightNode = newNode(12);
	root->leftNode->rightNode->leftNode = newNode(10);
	root->leftNode->rightNode->rightNode = newNode(14);

	int n1 = 10, n2 = 14;
	struct node *t = lca(root, n1, n2);
	printf("LowestCommonAncestor of %d and %d is %d \n", n1, n2, t->data);

	n1 = 14, n2 = 8;
	t = lca(root, n1, n2);
	printf("LowestCommonAncestor of %d and %d is %d \n", n1, n2, t->data);

	n1 = 10, n2 = 22;
	t = lca(root, n1, n2);
	printf("LowestCommonAncestor of %d and %d is %d \n", n1, n2, t->data);

	getchar();
	return 0;
}