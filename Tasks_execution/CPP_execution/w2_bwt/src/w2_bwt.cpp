#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
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
			cout << s << endl;
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

		char GetLastSymbolIndex() const {
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



int main() {
	string text = "AGACATA";
	//cin >> text;

	for (int i = 0; i < 150; ++i) {
		text += "G";
	}
	text += "$";
	cout << text << endl;

	BurrowsWheelerTransformer transformer = BurrowsWheelerTransformer(text);
	string bwt = transformer.Transform();
	cout << bwt.length() << endl;
	cout << bwt << endl;

	return 0;
}
