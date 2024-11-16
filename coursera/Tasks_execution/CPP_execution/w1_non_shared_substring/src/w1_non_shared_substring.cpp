#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

struct Node
{
	vector<int> next;
	int startPosition = -1;
	int length = 0;
	string pathText = "";
	int notFromSecondText = 1;
};

struct ShortestSubstringContainer
{
	string substring = "";
};

typedef vector<Node> SuffixTree;

void PrintSuffixTree(const SuffixTree& tree, const string& text) {
	for (int i = 0; i < (int) tree.size(); ++i) {
	  Node node = tree[i];
	  cout << "index: " << i
		   << ", startPosition: " << node.startPosition
		   << ", length: " << node.length;
	  for (int next_index : node.next) {
		  cout << ", next: " << next_index;
	  }
	  if (node.length > 0) {
		  string suffix = text.substr(node.startPosition, node.length);
		  cout << ", suffix: " << suffix;
	  }
	  cout << endl;
  }
}

int AddNewNode(SuffixTree& tree, int parentNodeIndex, int startPosition, int length) {
	int newNodeIndex = tree.size();
	tree[parentNodeIndex].next.push_back(newNodeIndex);
	Node new_node;
	new_node.startPosition = startPosition;
	new_node.length = length;
	tree.push_back(new_node);
	return newNodeIndex;
}

SuffixTree BuildSuffixTree(const string& text) {
	SuffixTree tree;
	tree = { Node() };
	for (int textStartPosition = 0; textStartPosition < (int) text.size(); ++textStartPosition) {

//		PrintSuffixTree(tree, text);
//		cout << "=================================" << endl;

		int currentNodeIndex = 0;
		int currentNodeCurrentSymbolIndex = 0;

		for (int currentSuffixCurrentSymbolIndex = textStartPosition; currentSuffixCurrentSymbolIndex < (int) text.size(); ++currentSuffixCurrentSymbolIndex) {
			if (currentNodeCurrentSymbolIndex < tree[currentNodeIndex].length) {
				if ( text[ tree[currentNodeIndex].startPosition + currentNodeCurrentSymbolIndex ] != text[currentSuffixCurrentSymbolIndex] ) {
					// mismatch => split branch onto 2 ones:
					int old_length = tree[currentNodeIndex].length;
					tree[currentNodeIndex].length = currentNodeCurrentSymbolIndex;

					auto next = tree[currentNodeIndex].next;
					tree[currentNodeIndex].next.clear();

					int extraNodeIndex = AddNewNode(	tree,
														currentNodeIndex,
														tree[currentNodeIndex].startPosition + currentNodeCurrentSymbolIndex,
														old_length - currentNodeCurrentSymbolIndex);
					tree[extraNodeIndex].next = next;

					// and start a new branch (third one)!
					currentNodeIndex = AddNewNode(	tree,
													currentNodeIndex,
													currentSuffixCurrentSymbolIndex,
													1);
					currentNodeCurrentSymbolIndex = 1;
				} else {
					// just move by symbols of this node!
					++currentNodeCurrentSymbolIndex;
				}
			} else {
				// it is time to change the node
				int nextNodeIndex = -1;
				for (int i = 0; i < (int) tree[currentNodeIndex].next.size(); ++i) {
					if (text[ tree[ tree[currentNodeIndex].next[i] ].startPosition ] == text[currentSuffixCurrentSymbolIndex]) {
						nextNodeIndex = tree[currentNodeIndex].next[i];
						break;
					}
				}
				if (nextNodeIndex > -1) {
					currentNodeIndex = nextNodeIndex;
					currentNodeCurrentSymbolIndex = 1;
				} else {
					if (tree[currentNodeIndex].next.size() == 0 && tree[currentNodeIndex].startPosition != -1) {
						++tree[currentNodeIndex].length;
						++currentNodeCurrentSymbolIndex;
					} else {
						currentNodeIndex = AddNewNode(	tree,
														currentNodeIndex,
														currentSuffixCurrentSymbolIndex,
														1);
						currentNodeCurrentSymbolIndex = 1;
					}
				}
			}
		}
	}
	return tree;
}

// https://stackoverflow.com/questions/12607512/shortest-uncommon-substring-shortest-substring-of-one-string-that-is-not-a-sub
string TraverseBFS(const SuffixTree& tree, const string& text) {
	queue<Node> q;
	q.push(tree[0]);
	string backup = text.substr(0, 1);

	while (!q.empty()) {
		Node node = q.front();
		q.pop();

		string currentNodeSuffix = "";
		if (node.length > 0) {
			currentNodeSuffix = text.substr(node.startPosition, node.length);
		}
		cout << "Current node suffix: " << currentNodeSuffix << endl;
		cout << "Parent path: " << node.pathText << endl;

		if ( (int) currentNodeSuffix.find("#") > 0 ) {
			cout << "Answer 1: " << node.pathText + currentNodeSuffix.substr(0, 1) << endl;
			return node.pathText + currentNodeSuffix.substr(0, 1);
		}

		if (node.next.size() > 0) {
			bool text2Leaf = false;
			bool someLeaves = false;
			for (int index : node.next) {
				Node childNode = tree[index];
				childNode.pathText = node.pathText + currentNodeSuffix;
				q.push(childNode);
				string childText = text.substr(childNode.startPosition, childNode.length);

				if ( ((int) childText.find("$") > -1) && ((int) childText.find("#") == -1)  ) {
					text2Leaf = true;
				}

				if ((int) childText.find("$") > -1) {
					someLeaves = true;
				}
			}

//			if (someLeaves && !text2Leaf) {
//				cout << "Answer 2: " << node.pathText + currentNodeSuffix << endl;
//				return node.pathText + currentNodeSuffix;
//			}
		}
	}

	cout << "Backup: " << backup << endl;
	return backup;
}

// https://github.com/barik111/Data-Structures-and-Algorithms-Specialization/blob/master/Data_Structures_and_Algorithms/Algorithms_on_Strings/Programming-Assignment-1/non_shared_substring/NonSharedSubstring.java
int TraverseDFS(int currentNodeIndex, const SuffixTree& tree, const string& text, int textsDelimiterPosition, string pathText, ShortestSubstringContainer& container) {
	Node node = tree[currentNodeIndex];
	if (node.next.size() == 0) {
		// it is a leaf.
		node.notFromSecondText = node.startPosition < textsDelimiterPosition + 1 ? 1 : 0;
	} else {
		for (int index : node.next) {
			string currentNodeSuffix = "";
			if (node.length > 0) {
				currentNodeSuffix = text.substr(node.startPosition, node.length);
			}
			node.notFromSecondText *= TraverseDFS(index, tree, text, textsDelimiterPosition, pathText + currentNodeSuffix, container);
		}
	}

	if (node.notFromSecondText == 1) {
		node.pathText = pathText;

		if (node.startPosition < textsDelimiterPosition) {
			node.pathText += text.substr(node.startPosition, 1);
			if (container.substring.length() == 0 || container.substring.length() > node.pathText.length()) {
				container.substring = node.pathText;
			}
		}
	}
	return node.notFromSecondText;
}

string solve (string p, string q)
{
	string result = p;
	string text = p + '#' + q + '$';
	//cout << text << endl << endl;
	SuffixTree tree = BuildSuffixTree(text);
	//PrintSuffixTree(tree, text);
	ShortestSubstringContainer container;
	TraverseDFS(0, tree, text, p.length(), "", container);
	return container.substring;
}

int main (void)
{
	string p; // = "ATGCGATGACCTGACTGA"; // "AAAAAAAAAAAAAAAAAAAA"; // "ATGCGATGACCTGACTGA"; // "CCAAGC"; // "CCAAGCTGCTAGAGG"; // "AT"; // "AAAA"; // "AA"; // "A"; // "AAA"; // "AAT"; // "ATAATT";
	cin >> p;
	string q; // = "CTCAACGTATTGGCCAGA"; // "TTTTTTTTTTTTTTTTTTTT"; // "CTCAACGTATTGGCCAGA"; // "CATGCT"; // "CATGCTGGGCTGGCT"; // "TT"; // "TTTT"; // "AT"; // "T"; // "TAA"; // "AT"; // "ATT";
	cin >> q;

	string ans = solve(p, q);
	cout << ans << endl;

	return 0;
}

