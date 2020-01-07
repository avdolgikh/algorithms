#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstdio>
#include <sstream>

using namespace std;

void PrintCounts(const vector<char>& symbols, int length, const map<char, vector<int>>& occ_count_before) {
	for (auto& symbol : symbols) {
		cout << symbol << "   ";
	}
	cout << endl;
	for (int i = 0; i < length; ++i) {
		for (auto& symbol : symbols) {
			cout << occ_count_before.at(symbol)[i] << "   ";
		}
		cout << endl;
	}
}

// Preprocess the Burrows-Wheeler Transform bwt of some text
// and compute as a result:
//   * starts - for each character C in bwt, starts[C] is the first position
//       of this character in the sorted array of
//       all characters of the text.
//   * occ_count_before - for each character C in bwt and each position P in bwt,
//       occ_count_before[C][P] is the number of occurrences of character C in bwt
//       from position 0 to position P inclusive.
void PreprocessBWT(const string& bwt,
                   map<char, int>& starts,
                   map<char, vector<int> >& occ_count_before) {
	map<char, int> symbolCounts;
	vector<char> symbols;

	for (size_t i = 0; i < bwt.length(); ++i) {
		symbolCounts[bwt[i]]++;

		if (occ_count_before[bwt[i]].empty()) {
			vector<int> zeros(bwt.length(), 0);
			occ_count_before[bwt[i]] = zeros;
		}

		for (auto const& symbol : symbolCounts) {
			occ_count_before[symbol.first][i] = symbolCounts[symbol.first];
		}
	}

	for (auto const& symbol : symbolCounts) {
		symbols.push_back(symbol.first);
	}

	PrintCounts(symbols, (int) bwt.length(), occ_count_before);

	int firstColumnIndex = 0;
	for (auto& symbol : symbols) {
		//cout << counts[symbol] << endl;
		starts[symbol] = firstColumnIndex;
		firstColumnIndex += symbolCounts[symbol];
		cout << "starts[" << symbol << "]: " << starts[symbol] << endl;
	}
}

// Compute the number of occurrences of string pattern in the text
// given only Burrows-Wheeler Transform bwt of the text and additional
// information we get from the preprocessing stage - starts and occ_counts_before.
int CountOccurrences(const string& pattern,
                     const string& bwt,
                     const map<char, int>& starts,
                     const map<char, vector<int> >& occ_count_before) {
  int top = 0;
  int bottom = bwt.length() - 1;
  int symbolIndex = pattern.length() - 1;
  while (top <= bottom) {
	  if (symbolIndex >= 0) {
		  char symbol = pattern[symbolIndex];
		  --symbolIndex;
		  cout << "pattern symbol: " << symbol << endl;
		  bool contains = false;
		  for (int i = top; i <= bottom; ++i) {
			  //cout << "i: " << i << ", bwt[i]: " << bwt[i] << endl;
			  if (symbol == bwt[i]) {
				  //cout << "starts.at(symbol): " << starts.at(symbol) << endl;
				  //cout << "occ_count_before.at(symbol)[top]: " << occ_count_before.at(symbol)[top] << endl;
				  //cout <<  "occ_count_before.at(symbol)[bottom]: " << occ_count_before.at(symbol)[bottom] << endl;
				  int topCount = occ_count_before.at(symbol)[top] > 0 ? occ_count_before.at(symbol)[top] - 1 : 0;
				  int bottomCount = occ_count_before.at(symbol)[bottom] > 0 ? occ_count_before.at(symbol)[bottom] - 1 : 0;
				  top = starts.at(symbol) + topCount;
				  bottom = starts.at(symbol) + bottomCount;
				  cout << "top: " << top << endl;
				  cout << "bottom: " << bottom << endl;
				  contains = true;
				  break;
			  }
		  }
		  if (!contains) {
			  return 0;
		  }
	  } else {
		  return bottom - top + 1;
	  }
  }
  return 0;
}


int main() {
  string bwt = "AGGGAA$";
  //cin >> bwt;
  int pattern_count = 1;
  //cin >> pattern_count;

  // Start of each character in the sorted list of characters of bwt,
  // see the description in the comment about function PreprocessBWT
  map<char, int> starts;

  // Occurrence counts for each character and each position in bwt,
  // see the description in the comment about function PreprocessBWT
  map<char, vector<int> > occ_count_before;

  // Preprocess the BWT once to get starts and occ_count_before.
  // For each pattern, we will then use these precomputed values and
  // spend only O(|pattern|) to find all occurrences of the pattern
  // in the text instead of O(|pattern| + |text|).
  PreprocessBWT(bwt, starts, occ_count_before);

  for (int pi = 0; pi < pattern_count; ++pi) {
    string pattern = "GA";
    //cin >> pattern;
    int occ_count = CountOccurrences(pattern, bwt, starts, occ_count_before);
    printf("%d ", occ_count);
  }
  printf("\n");
  return 0;
}

