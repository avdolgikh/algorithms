#include <map>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

typedef map<char, int> edges;
typedef vector<edges> trie;

trie build_trie(const vector<string> & patterns) {
  trie t;
  t = { {} };
  for (const auto& pattern : patterns) {
	  //cout << pattern << endl;
	  int current_node = 0;
	  for (const char& c : pattern) {
		  //cout << c << endl;
		  if (t[current_node].count(c) > 0) {
			  //cout << "!" << endl;
			  current_node = t[current_node][c];
		  } else {
			  //cout << t.size() << endl;
			  int new_node = t.size();
			  t[current_node][c] = new_node;
			  t.push_back({});
			  current_node = new_node;
		  }
	  }
  }
  return t;
}

int main() {
  int n = 1;
  cin >> n;
  vector<string> patterns;
  //vector<string> patterns = { "ATA" };
  //vector<string> patterns = { "AT", "AG", "AC" };
  //vector<string> patterns = { "ATAGA", "ATC", "GAT" };
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    patterns.push_back(s);
  }

  trie t = build_trie(patterns);
  //cout << t.size() << endl;
  for (size_t i = 0; i < t.size(); ++i) {
    for (const auto & j : t[i]) {
      cout << i << "->" << j.second << ":" << j.first << "\n";
    }
  }

  return 0;
}
