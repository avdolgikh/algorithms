#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

struct Node
{
	vector<int> next;
	int startPosition = -1;
	int length = 0;
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

vector<string> ComputeSuffixTreeEdges(const string& text) {
  vector<string> result;
  SuffixTree tree = BuildSuffixTree(text);
  //PrintSuffixTree(tree, text);
  for (const Node& node : tree) {
	  if (node.length > 0) {
		string suffix = text.substr(node.startPosition, node.length);
		result.push_back( suffix );
	  }
  }
  return result;
}

int main() {
  string text = "panamabananas$"; //"panamabananas$"; //"ATAAATG$"; //"ACA$"; //"A$";
  //cin >> text;
  vector<string> edges = ComputeSuffixTreeEdges(text);
  for (int i = 0; i < (int) edges.size(); ++i) {
    cout << edges[i] << endl;
  }
  return 0;
}
