#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstdio>
#include <sstream>

using namespace std;

void PrintCounts(const map<char, int>& symbolCounts, int length, const map<char, vector<int>>& occ_count_before) {
	for (auto& symbol : symbolCounts) {
		cout << symbol.first << "   ";
	}
	cout << endl;
	for (int i = 0; i < length; ++i) {
		for (auto& symbol : symbolCounts) {
			cout << occ_count_before.at(symbol.first)[i] << "   ";
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

	for (size_t i = 0; i < bwt.length(); ++i) {
		symbolCounts[bwt[i]]++;

		if (occ_count_before[bwt[i]].empty()) {
			occ_count_before[bwt[i]].assign(bwt.length(), 0);
		}

		vector<int> tailCounts(bwt.length() - i, symbolCounts[bwt[i]]);
		copy( begin(tailCounts), end(tailCounts), begin(occ_count_before[bwt[i]]) + i);
	}

	int firstColumnIndex = 0;
	for (auto& symbolCount : symbolCounts) {
		starts[symbolCount.first] = firstColumnIndex;
		firstColumnIndex += symbolCount.second;
		//cout << "starts[" << symbolCount.first << "]: " << starts[symbolCount.first] << endl;
	}

	//PrintCounts(symbolCounts, (int) bwt.length(), occ_count_before);
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
		  //cout << "pattern symbol: " << symbol << endl;
		  bool contains = false;
		  for (int i = top; i <= bottom; ++i) {
			  if (symbol == bwt[i]) {
				  int topCount = occ_count_before.at(symbol)[top] > 0 ? occ_count_before.at(symbol)[top] - 1 : 0;
				  int bottomCount = occ_count_before.at(symbol)[bottom] > 0 ? occ_count_before.at(symbol)[bottom] - 1 : 0;
				  top = starts.at(symbol) + topCount;
				  bottom = starts.at(symbol) + bottomCount;
				  //cout << "top: " << top << endl;
				  //cout << "bottom: " << bottom << endl;
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
  string bwt; // = "smnpbnnaaaaa$a";
  cin >> bwt;
  int pattern_count;
  cin >> pattern_count;

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
    string pattern; // = "ana";
    cin >> pattern;
    int occ_count = CountOccurrences(pattern, bwt, starts, occ_count_before);
    printf("%d ", occ_count);
  }
  printf("\n");
  return 0;
}

