from collections import deque


class Node:
    """
    Class to represent a Node in a Trie data structure

    Written By: Chan Yanhan

    Code inspired by Lecture Materials from FIT2004 Monash Malaysia
    """

    def __init__(self, data=None, size=27):
        """
        Constructor of the Node class

        Input:
            data: the data to be stored in the Node
            size: the size of the link array 

        Return:
            None

        S = size of link array 

        Time complexity: 
            Best:   O(1) if size is None, otherwise O(S)
            Worst:  O(1) if size is None, otherwise O(S)

        Space complexity: 
            Input:  O(1)
            Aux:    O(S)
        """
        self.data = data
        self.link = [None] * size
        self.occurance = 0
        self.next = None


class CatsTrie:
    """
    Class to represent a Trie data structure

    Written By: Chan Yanhan

    Code inspired by Lecture Materials from FIT2004 Monash Malaysia
    """

    def __init__(self, sentences):
        """
        Constructor of the CatsTrie class

        Input:
            sentences: a list of strings representing cat sentences

        Return:
            None

        N = number of sentence in the sentences
        M = number of characters in of the longest sentence in sentences

        Time complexity: 
            Best:   O(N*M)
            Worst:  O(N*M)

        Space complexity: 
            Input:  O(N*M)
            Aux:    O(N*M)
        """
        self.root = Node()
        self.sentences = sentences
        self.construct_trie(self.sentences)

    def construct_trie(self, sentences):
        """
        Function Description:
        This function is a helper function to construct the CatsTrie data structure

        Approach Description:
        Iterate through the list of sentences and inserting every sentence into the CatsTrie data structure by calling the insert method of the CatsTrie class. 

        Input:
            sentences: a list of strings where each string represents a cat sentence

        Return:
            None

        N = number of sentence in sentences
        M = number of characters of the longest sentence in sentences

        Time complexity: 
            Best:   O(N * M)
            Worst:  O(N * M)

        Space complexity: 
            Input:  O(N * M)
            Aux:    O(N * M)
        """
        for sentence in sentences:
            self.insert(sentence)
        return

    def insert(self, sentence):
        """
        Function Description:
        This function inserts a given sentence as input, into the CatsTrie

        Input:
            sentence: a string representing a cat sentence

        Return:
            None

        M = number of characters in sentence

        Time complexity: 
            Best:   O(M)
            Worst:  O(M)

        Space complexity: 
            Input:  O(M)
            Aux:    O(M) - due to recursion stack
        """
        current = self.root
        self.insert_aux(current, sentence, 0)
        return

    def insert_aux(self, current, sentence, i):
        """
        Function Description:
        This function inserts all characters of a sentence into the CatsTrie data structure.

        Approach Description:
        Since each node have a link array where if node.link[i] is not None, node.link[i] represents a Node representing the ith letter of the alphabets. For instance, node.link[2] represents the second letter of the alphabets, which is the letter 'b'. Also a terminating character is inserted at the 0th index of the link array and if at 0th index of the link array is not None, this indicates that the characters from the root to the current node makes up to a sentence which exists in the list of sentences. 

        Using recursion, each character of the sentence would be used as an index of the link array of the node to check if the character exists. If it does not exists, a new node would be generated and stored at the node's link array. Then each character would be inserted recursively until a terminating condtition is reached where all characters of the sentence is inserted. Then on the return of each recursive call, the occurrance of the word being inserted would be updated. Each node would store the next child node that has occurred the most and also the number of occurrances. In the case where two characters have the same number of occurances, the lexicographical smaller word would be favoured. 

        Input:
            current: a Node object
            sentence: the sentence to be inserted to the CatsTrie
            i: an integer representing the index of the current character to be inserted

        Return:
            an integer representing the number of occurrances the current sentence is occur in the CatsTrie

        M = number of characters of sentence

        Time complexity: 
            Best:   O(M)
            Worst:  O(M)

        Space complexity: 
            Input:  O(M)
            Aux:    O(M) - due to recursion stack 
        """
        if i == len(sentence) + 1:
            current.occurance += 1
            return current.occurance

        else:
            # for determination of $ or not
            index = 0 if i == len(sentence) else ord(sentence[i]) - 97 + 1

            # for checking if we need to create a new node during insert
            if current.link[index] is None:
                current.link[index] = Node(data=index)

            inserted_word_occurance = self.insert_aux(
                current.link[index], sentence, i+1)

            # update the occurance
            if current.occurance < inserted_word_occurance:
                current.occurance = inserted_word_occurance
                current.next = current.link[index]

            # choose the one with lower lexicographical order
            elif current.occurance == inserted_word_occurance and current.link[index].data < current.next.data:
                current.next = current.link[index]

            return inserted_word_occurance

    def search(self, key):
        """
        Function Description:
        This function search and traverse the CatsTrie to look for the Node representing key[N] where the Node has a prefix of key[1...N-1]. For instance, key = "acb", this function would search for the node representing "b" that also have a prefix of "ac". It also return a list of characters if all characters in key are present in the CatsTrie, otherwise return None. 

        Input:
            key: a string to be searched in the CatsTrie

        Return:
            arr: a list containing characters
            current: a Node object 

        M = number of characters in key

        Time complexity: 
            Best:   O(1) where the first character of the key does not exist in the CatsTrie
            Worst:  O(M)

        Space complexity: 
            Input:  O(M)
            Aux:    O(M)
        """
        arr = []
        current = self.root
        for char in key:
            index = ord(char) - 97 + 1
            if current.link[index]:
                arr.append(char)
                current = current.link[index]
            else:
                return None, None
        return arr, current

    def autoComplete(self, prompt):
        """
        Function Description:
        This function acts as an autocomplete feature for a prompt. The autocompleted string is determined based on the frequency of the sentences in the list of sentences.

        Approach Description:
        Given a list of sentences before hand, a Trie data structure would be constructed. For each characters in every sentence in the list of sentences, it would be inserted to the Trie data structure. In the trie, the characters would be represented as a Node. During the insertion process, the information of the frequencies of the inserted sentence would be saved. 

        Then given the prompt, it would first search for the sentence in the Trie that has the prefix equivalent to the prompt. If it does not exist, this function would return None.

        Otherwise, using the Node returned from the search function, it would traverse down the Trie using information stored during the insertion process, to complete and return the sentence. 

        Input:
            prompt:
            a string with characters in the set of [a, b, c, ....z] representing the incomplete sentence to be autocompleted

        Return:
            None, if the prompt does not exist in the list of sentences in the CatsTrie, 
            otherwise a autocompleted string that has the highest frequency in the list of sentences

        X = length of the prompt
        Y = length of the most frequent sentence in the list of senetences in the CatsTrie that have a prefix of the prompt

        Time Complexity: 
            Best:
            O(1) where the prompt does not exist in the list of sentences and all sentences in the list of sentences does not start with the first character of the prompt. 

            Worst:
            O(X + Y)

        Space complexity: 
            Input:  O(X)

            Aux:
            O(X + Y) for the list that stores the characters from the prompt and the autocompleted string

        """
        return_arr, current = self.search(prompt)
        if return_arr is None:
            return return_arr

        current = current.next
        while current.data != 0:
            return_arr.append(chr(current.data + 97 - 1))
            current = current.next
        return "".join(return_arr)


# ==================== Main Functions ====================
if __name__ == "__main__":

    # Sample Test
    sentences = ["abc",
                 "abazacy",
                 "dbcef",
                 "xzz",
                 "gdbc",
                 "abazacy",
                 "xyz",
                 "abazacy",
                 "dbcef",
                 "xyz",
                 "xxx",
                 "xzz"]
    mycattrie = CatsTrie(sentences)
    prompt = "x"
    print("Auto completed:", str(mycattrie.autoComplete(prompt)))
