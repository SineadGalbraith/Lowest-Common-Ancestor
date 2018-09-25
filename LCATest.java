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
	}
}