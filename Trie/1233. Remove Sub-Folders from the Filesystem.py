Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
 

Constraints:

1 <= folder.length <= 4 * 104
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'.
folder[i] always starts with the character '/'.
Each folder name is unique.


# Trie Tree
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isFolder = False
        self.folder = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, folder):
        node = self.root
        
        for char in folder:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
        
        node.isFolder = True
        node.folder = folder
        
        return
    
    def find(self, folder):
        node = self.root
        
        for char in folder:
            # Change the find function for specific use case
            if char not in node.children:
                return False
            
            if node.children[char].isFolder:
                return True
            
            node = node.children[char]
        
        return True

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        # Edge case: ["/ah/al/am","/ah/al"]
        # If not sort, we will firstly add "/ah/al/am" into trie tree, then add "/ah/al"
        # Wrong output: ["/ah/al/am","/ah/al"]; Expected output: ["/ah/al"]
        folders.sort()
        
        trie = Trie()
        res = []
        for folder in folders:
            # Edge case: ["/a/b/c","/a/b/ca","/a/b/d"]
            # If not follow '/' to split, the for loop of the char will be '/ a / b / c a', 
            # so "/a/b/ca" will be the sub-folder of "/a/b/c"
            # Wrong output: ["/a/b/c","/a/b/d"]; Expected output: ["/a/b/c","/a/b/ca","/a/b/d"]
            folder_list = folder.split('/')
            if trie.find(folder_list):
                continue
            
            res.append(folder)
            trie.add(folder_list)
        
        return res
        

# Math
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/5964641/Explained-step-by-step-or-Beats-100-or-Working-25.10.2024
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder:
            return []
        
        folder.sort()
        
        res = []
        res.append(folder[0])
        
        for i in range(1, len(folder)):
            # 1. prev should use res[-1] not folder[i - 1], because we need to compare with lastest result folder, not the lastest folder
            # Sample: ["/a","/a/b/c","/a/b/d"]
            # folder[i - 1] = "/a/b/c" -> "/a/b/d" is not sub-folder
            # res[-1] = "/a" -> "/a/b/d" is sub-folder
            # Wrong output: ["/a","/a/b/d"]; Expected output: ["/a"]

            # 2. need to ' + '/'' when comparing 
            # Edge case: ["/a/b/c","/a/b/ca","/a/b/d"]
            # If not add '/', "/a/b/ca" will be the sub-folder of "/a/b/c"
            prev, curt = res[-1] + '/', folder[i]
            
            if not curt.startswith(prev):
                res.append(curt)
            
        return res
        
