/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void fun(TreeNode *root,int &r,vector<int>&v)
    {
        //if(root!=NULL)
        r=(r*10)+root->val;
        if(root->left==NULL and root->right==NULL)
        {
            v.push_back(r);
            //cout<<r<<" ";
            return;
        }
        
        if(root->left){fun(root->left,r,v);
         r/=10;}
        if(root->right){fun(root->right,r,v);
        r/=10;}
       
    }
    int sumNumbers(TreeNode* root) {
        int r=0;
        vector<int>v;
        fun(root,r,v);
        int ans=0;
        for(auto it:v)
        ans+=it;
        return ans;
    }
};