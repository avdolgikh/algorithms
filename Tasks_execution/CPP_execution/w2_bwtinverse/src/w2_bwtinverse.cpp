#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

class BurrowsWheelerTransformer {
public:
	BurrowsWheelerTransformer (const string& original_text) {
		text = original_text;
		Preprocess();
	}

	string Transform() const {
		string bwt = "";
		for (const auto& item : items) {
			char s = text[ item.GetLastSymbolIndex() ];
			//cout << s << endl;
			bwt.push_back(s);
		}
		return bwt;
	}

	static string Rotate(const string& text, int firstSymbolIndex) {
		return text.substr(firstSymbolIndex, text.length() - firstSymbolIndex) + text.substr(0, firstSymbolIndex);
	}

private:
	class Element {
	public:
		Element (const string& originalText,  int firstSymbolIndex) {
			// TODO: check that memory is not allocated for "text"
			text = originalText;
			firstSymbolInd = firstSymbolIndex;
			lastSymbolInd = firstSymbolInd == 0 ? text.length() - 1 : firstSymbolInd - 1;
		}

		bool operator < (const Element& obj ) {
			return Rotate(text, firstSymbolInd) < Rotate(text, obj.firstSymbolInd);
		}

		int GetLastSymbolIndex() const {
			return lastSymbolInd;
		}

	private:
		int lastSymbolInd;
		int firstSymbolInd;
		string text;
	};

	void Preprocess() {
		for (int i = 0; i < text.length(); ++i) {
			items.push_back( Element(text, i) );
		}
		sort(begin(items), end(items));
	}

	string text;
	vector<Element> items;
};

string InverseBWT(const string& bwt) {
	vector<string> encoded;
	map<string, int> sorted;

	for (int i = 0; i < bwt.length(); ++i) {
		char current = bwt[i];
		string code = to_string( i );
		code = string(6 - code.length(), '0') + code;
		encoded.push_back( current + code );
	}

	{
		vector<string> encodedAlphaBet = encoded;
		sort(begin(encodedAlphaBet), end(encodedAlphaBet));

		for (int i = 0; i < encodedAlphaBet.size(); ++i) {
			//cout << encodedAlphaBet[i] << endl;
			sorted[ encodedAlphaBet[i] ] = i;
		}
	}

	string text = "$";
	string current = encoded[0];
	for (int i = 0; i < bwt.length() - 1; ++i) {
		//cout <<  current[0] << endl;
		text.push_back( current[0] );
		current = encoded[ sorted[ current ] ];
	}

	reverse(begin(text), end(text));
	return text;
}

int main() {
	//string text = "AGdasdsgergrAnttCnAshnyvulerTrgri8oujyA$";
	//cout << text << endl;
	//BurrowsWheelerTransformer transformer = BurrowsWheelerTransformer(text);
	//string bwt = transformer.Transform();
	//cout << bwt << endl;

	string bwt = "AGGGAA$";
//	for (int i = 0; i < 100000; ++i) {
//		bwt += "T";
//	}
	//cin >> bwt;
	cout << InverseBWT(bwt) << endl;

  return 0;
}
