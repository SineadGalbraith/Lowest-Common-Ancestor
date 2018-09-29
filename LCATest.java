import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class LCATest {

	@Test
	public void test() {
		LCA tree = new LCA();
		
		// Tree with 3 elements
		//  1
		// / \
		//2   3
		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.right = new Node(3);
		
		assertEquals(1, tree.findLCA(2, 3));
		
		tree = new LCA();
		// Tree with multiple elements
		//  		 1
		// 			/ \
		//	  	   2   3
		//   	  /   
		//		 4  
		//	    / \
		//	   5   6
		//	  / \
		//   7   8
		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.right = new Node(3);
		tree.root.left.left = new Node(4);
		tree.root.left.left.left = new Node(5);
		tree.root.left.left.right = new Node(6);
		tree.root.left.left.left.left = new Node(7);
		tree.root.left.left.left.right = new Node(8);

		assertEquals(5,tree.findLCA(7, 8));
		assertEquals(4, tree.findLCA(6, 8));
		
		tree = new LCA();
		// Tree with multiple elements
		//  		   1
		// 			/ 	  \
		//	  	   2   	   3
		//   	  /       / \
		//		 4       9   10
		//	    / \     / \   
		//	   5   6   11 13
		//	  / \	  /
		//   7   8   12
		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.right = new Node(3);
		tree.root.left.left = new Node(4);
		tree.root.left.left.left = new Node(5);
		tree.root.left.left.right = new Node(6);
		tree.root.left.left.left.left = new Node(7);
		tree.root.left.left.left.right = new Node(8);
		tree.root.right.left = new Node(9);
		tree.root.right.right = new Node(10);
		tree.root.right.left.left = new Node(11);
		tree.root.right.left.left.left = new Node(12);
		tree.root.right.left.right = new Node(13);
		
		assertEquals(9, tree.findLCA(12, 13));
		assertEquals(3, tree.findLCA(12, 10));
		assertEquals(1, tree.findLCA(8, 12));
		
		tree = new LCA();
		/* Tree with large amount of nodes
		 *							           1
		 * 						    /					  \
		 * 						   2					  14
		 * 						 /   \					/	 \
		 *						4     5				   16	  15
		 *					   / \   / \			  /  \    / \
		 *					  6   7 12 13			17   18  19  20
		 * 					 /    				    /\      /  \
		 * 					8					  21  22   23  24
		 * 				   / \					  /    \
		 * 				  10  11 				 25		26
		 * 				 
		*/			
		
		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.left.left = new Node(4);
		tree.root.left.right = new Node(5);
		tree.root.left.right.left = new Node(12);
		tree.root.left.right.right = new Node(13);
		tree.root.left.left.left = new Node(6);
		tree.root.left.left.right = new Node(7);
		tree.root.left.left.left.left = new Node(8);
		tree.root.left.left.left.left.left = new Node(10);
		tree.root.left.left.left.left.right = new Node(11);
		tree.root.right = new Node(14);
		tree.root.right.right = new Node(15);
		tree.root.right.left = new Node(16);
		tree.root.right.left.left = new Node(17);
		tree.root.right.left.right = new Node(18);
		tree.root.right.right.left = new Node(19);
		tree.root.right.right.right = new Node(20);
		tree.root.right.left.left.left = new Node(21);
		tree.root.right.left.left.right = new Node(22);
		tree.root.right.right.left.left = new Node(23);
		tree.root.right.right.left.right = new Node(24);
		tree.root.right.left.left.left.left = new Node(25);
		tree.root.right.left.left.right.right = new Node(26);
		
		assertEquals(1, tree.findLCA(10, 26));
		assertEquals(17, tree.findLCA(25, 26));
		assertEquals(2, tree.findLCA(11, 12));
		assertEquals(14, tree.findLCA(18, 24));
		assertEquals(4, tree.findLCA(7, 11));
	}
}
