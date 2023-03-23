#include <iostream>
#include <queue>
#include <vector>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode()
        : val(0), left(nullptr), right(nullptr)
    {
    }

    TreeNode(int x)
        : val(x), left(nullptr), right(nullptr)
    {
    }

    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right)
    {
    }
};

TreeNode *invertTree(TreeNode *root)
{
    if (root != nullptr)
    {
        auto temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(temp);
    }
    return root;
}

TreeNode *vectorToTree(
    std::vector<int>::const_iterator begin,
    std::vector<int>::const_iterator end)
{
    if (begin == end)
    {
        return nullptr;
    }

    auto left_it = begin + 1 == end ? begin + 1 : end;
    auto right_it = left_it + 1 == end ? left_it + 1 : end;

    return new TreeNode(
        *begin,
        vectorToTree(left_it, end),
        vectorToTree(right_it, end));
}

TreeNode *vectorToTree(std::vector<int> treevec)
{
    return vectorToTree(treevec.cbegin(), treevec.cend());
}

template <class T>
std::ostream &operator<<(std::ostream &os, const std::vector<T> &v)
{
    os << "[";
    auto penultimate = v.end() - 1;

    for (auto iter = v.begin(); iter != v.end(); ++iter)
    {
        os << *iter;
        if (iter != penultimate)
        {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

int main(int argc, char **argv)
{
    std::vector<int> sample1 = {4, 2, 7, 1, 3, 6, 9};
    std::vector<int> sample2 = {2, 1, 3};
    std::vector<int> sample3 = {};

    std::cout << "sample 1: " << sample1 << std::endl;
    auto tree1 = vectorToTree(sample1); // ain't nobody has time for free

    return 0;
};