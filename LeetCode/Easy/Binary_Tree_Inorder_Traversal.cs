/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    IList<int> l = new List<int>();
    public IList<int> InorderTraversal(TreeNode root)
    {
        if (root != null)
        {
            InorderTraversal(root.left);
            l.Add(root.val);
            InorderTraversal(root.right);
        }
        return l;
    }
}