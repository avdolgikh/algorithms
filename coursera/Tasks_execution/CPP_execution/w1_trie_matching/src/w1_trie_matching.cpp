#include <algorithm>
#include <cassert>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int const Letters =    4;
int const NA      =   -1;

struct Node
{
	int next [Letters];

	Node ()
	{
		fill (next, next + Letters, NA);
	}

	bool isLeaf () const
	{
	    return (next[0] == NA && next[1] == NA && next[2] == NA && next[3] == NA);
	}
};

typedef vector<Node> trie;

int letterToIndex (char letter)
{
	switch (letter)
	{
		case 'A': return 0; break;
		case 'C': return 1; break;
		case 'G': return 2; break;
		case 'T': return 3; break;
		default: assert (false); return -1;
	}
}

trie build_trie(const vector<string>& patterns) {
  trie t;
  t = { Node() };
  for (const auto& pattern : patterns) {
	  int current_node = 0;
	  for (const char& c : pattern) {
		  int letter_index = letterToIndex(c);
		  if (t[current_node].next[letter_index] != NA) {
			  current_node = t[current_node].next[letter_index];
		  } else {
			  int new_node = t.size();
			  t[current_node].next[letter_index] = new_node;
			  t.push_back(Node());
			  current_node = new_node;
		  }
	  }
  }
  return t;
}

bool MatchPrefixTrie(const string& text, int start_pos, trie t) {
	int current_node = 0;
	for (int i = start_pos; i < (int) text.size(); ++i) {
		char c = text[i];
		int letter_index = letterToIndex(c);

		if (t[current_node].isLeaf()) {
			return true;
		} else if (t[current_node].next[letter_index] != NA) {
			current_node = t[current_node].next[letter_index];
		} else {
			return false;
		}
	}

	if (t[current_node].isLeaf()) {
		return true;
	} else {
		return false;
	}
}

vector <int> solve (const string& text, int n, const vector<string>& patterns)
{
	vector <int> result;
	trie t = build_trie(patterns);

	for (int i = 0; i < (int) text.size(); ++i) {
		if (MatchPrefixTrie(text, i, t)) {
			result.push_back(i);
		}
	}
	return result;
}

void CheckTrie(const vector<string>& patterns) {
	trie t = build_trie(patterns);
	for (size_t i = 0; i < t.size(); ++i) {
		for (int j = 0; j < Letters; ++j) {
			if (t[i].next[j] != NA) {
				cout << i << "->" << t[i].next[j] << ":" << j << "\n";
			}
		}
	}
}

int main (void)
{
	string text;
	cin >> text;

	int n;
	cin >> n;

	vector<string> patterns(n);
	for (int i = 0; i < n; i++)
	{
		cin >> patterns[i];
	}

	vector <int> ans;
	ans = solve (text, n, patterns);

	for (int i = 0; i < (int) ans.size(); i++)
	{
		cout << ans[i];
		if (i + 1 < (int) ans.size())
		{
			cout << " ";
		}
		else
		{
			cout << endl;
		}
	}

	return 0;
}
