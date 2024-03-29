import static org.junit.jupiter.api.Assertions.*;
import static org.junit.Assert.*;
import static org.junit.Assert.assertTrue;

import org.junit.jupiter.api.Test;

class LCATest {

	@Test
	public void testLCA() {
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
		
		assertEquals(1, tree.findLCA(1, 26));
		assertEquals(1, tree.findLCA(10, 26));
		assertEquals(17, tree.findLCA(25, 26));
		assertEquals(2, tree.findLCA(11, 12));
		assertEquals(14, tree.findLCA(18, 24));
		assertEquals(4, tree.findLCA(7, 11));
		
		tree = new LCA();
		/* Tree with left nodes
		 * 			1
		 * 		   /
		 * 		  2
		 * 		 /
		 * 		3
		 * 	   / 
		 * 	  4
		 */
		
		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.left.left = new Node(3);
		tree.root.left.left.left = new Node(4);
		 
		assertEquals(2, tree.findLCA(4, 2));
		
		/*
		 * Code also being tested when node does not exist, should return -1
		 */
		assertEquals(-1, tree.findLCA(3, 5));
		
		/*
		 * Test for empty tree (should print -1, the same as above)
		 */
		
		tree = new LCA();
		assertEquals(-1, tree.findLCA(1, 3));
		
	}
	
	@Test
	public void testNode()
	{
		/*
		 * Test Node Class
		 * 
		 * When a node is created and given a value of 1 the data will become 1 and the left and right components will remain null.
		 */
		Node node = new Node(1);
		
		assertEquals(1, node.data);
		
		LCA tree = new LCA();
		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.right = new Node(3);
		
		assertEquals(2, tree.root.left.data);
		assertEquals(3, tree.root.right.data);
		
	}
}
