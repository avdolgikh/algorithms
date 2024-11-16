#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <cassert>
#include <cstdio>
#include <set>
#include <map>
#include <stack>

using namespace std;

struct Node
{
	vector<int> next;
	int chunkStartPosition = -1;
	int chunkLength = 0;
	int suffixPosition = -1;
};

typedef vector<Node> SuffixTree;

void PrintSuffixTree(const SuffixTree& tree, const string& text) {
	for (int i = 0; i < (int) tree.size(); ++i) {
	  Node node = tree[i];
	  cout << "index: " << i
		   << ", chunkStartPosition: " << node.chunkStartPosition
		   << ", chunkLength: " << node.chunkLength
		   << ", suffixPosition: " << node.suffixPosition;
	  for (int next_index : node.next) {
		  cout << ", next: " << next_index;
	  }
	  if (node.chunkLength > 0) {
		  string suffix = text.substr(node.chunkStartPosition, node.chunkLength);
		  cout << ", chunk: " << suffix;
	  }
	  cout << endl;
  }
}

int AddNewNode(SuffixTree& tree, int parentNodeIndex, int startPosition, int length, int suffixPosition) {
	int newNodeIndex = tree.size();
	tree[parentNodeIndex].next.push_back(newNodeIndex);
	Node new_node;
	new_node.chunkStartPosition = startPosition;
	new_node.chunkLength = length;
	new_node.suffixPosition = suffixPosition;
	tree.push_back(new_node);
	return newNodeIndex;
}

SuffixTree BuildSuffixTree(const string& text) {
	SuffixTree tree;
	tree = { Node() };
	for (int textStartPosition = 0; textStartPosition < (int) text.size(); ++textStartPosition) {

		int currentNodeIndex = 0;
		int currentNodeCurrentSymbolIndex = 0;

		for (int currentSuffixCurrentSymbolIndex = textStartPosition; currentSuffixCurrentSymbolIndex < (int) text.size(); ++currentSuffixCurrentSymbolIndex) {
			if (currentNodeCurrentSymbolIndex < tree[currentNodeIndex].chunkLength) {
				if ( text[ tree[currentNodeIndex].chunkStartPosition + currentNodeCurrentSymbolIndex ] != text[currentSuffixCurrentSymbolIndex] ) {
					// mismatch => split branch onto 2 ones:
					int old_length = tree[currentNodeIndex].chunkLength;
					tree[currentNodeIndex].chunkLength = currentNodeCurrentSymbolIndex;

					auto next = tree[currentNodeIndex].next;
					tree[currentNodeIndex].next.clear();

					int extraNodeIndex = AddNewNode(	tree,
														currentNodeIndex,
														tree[currentNodeIndex].chunkStartPosition + currentNodeCurrentSymbolIndex,
														old_length - currentNodeCurrentSymbolIndex,
														tree[currentNodeIndex].suffixPosition	);
					tree[extraNodeIndex].next = next;

					// and start a new branch (third one)!
					currentNodeIndex = AddNewNode(	tree,
													currentNodeIndex,
													currentSuffixCurrentSymbolIndex,
													1,
													textStartPosition	);
					currentNodeCurrentSymbolIndex = 1;
				} else {
					// just move by symbols of this node!
					++currentNodeCurrentSymbolIndex;
				}
			} else {
				// it is time to change the node
				int nextNodeIndex = -1;
				for (int i = 0; i < (int) tree[currentNodeIndex].next.size(); ++i) {
					if (text[ tree[ tree[currentNodeIndex].next[i] ].chunkStartPosition ] == text[currentSuffixCurrentSymbolIndex]) {
						nextNodeIndex = tree[currentNodeIndex].next[i];
						break;
					}
				}
				if (nextNodeIndex > -1) {
					currentNodeIndex = nextNodeIndex;
					currentNodeCurrentSymbolIndex = 1;
				} else {
					if (tree[currentNodeIndex].next.size() == 0 && tree[currentNodeIndex].chunkStartPosition != -1) {
						++tree[currentNodeIndex].chunkLength;
						++currentNodeCurrentSymbolIndex;
					} else {
						currentNodeIndex = AddNewNode(	tree,
														currentNodeIndex,
														currentSuffixCurrentSymbolIndex,
														1,
														textStartPosition	);
						currentNodeCurrentSymbolIndex = 1;
					}
				}
			}
		}
	}
	return tree;
}

void DFS(const SuffixTree& tree, vector<int>& leaves, const string& text) {
	stack<Node> s;
	s.push(tree[0]);

	while (!s.empty()) {
		Node node = s.top();
        s.pop();

        if (node.next.size() > 0) {
        	// sort node.next to reversed order of chunk first letter
        	sort(	begin(node.next), end(node.next),
					[text, tree] (int left, int right) {
						return text[ tree[left].chunkStartPosition ] > text[ tree[right].chunkStartPosition ];
					});
        	for (int index : node.next) {
				s.push( tree[index] );
        	}
        } else {
        	leaves.push_back(node.suffixPosition);
        }
	}
}

vector<int> BuildSuffixArray(const string& text) {
  vector<int> result;
  SuffixTree tree = BuildSuffixTree(text);
  PrintSuffixTree(tree, text);
  DFS(tree, result, text);
  return result;
}

int main() {
  string text = "AACGATAGCGGTAGA$";
  //cin >> text;
  vector<int> suffix_array = BuildSuffixArray(text);
  for (size_t i = 0; i < suffix_array.size(); ++i) {
    cout << suffix_array[i] << ' ';
  }
  cout << endl;
  return 0;
}
