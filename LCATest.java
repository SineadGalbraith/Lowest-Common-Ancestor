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
	}
}