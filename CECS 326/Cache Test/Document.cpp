#include "Document.h"
#include <cstdlib>
#include <string>

Document::Document() : mCharCount(rand() % 1048576 + 2097152)
{
	for (int i = 0; i < mCharCount; ++i) {
		int randVal = rand() % 26;
		char randChar = 'a' + randVal;
		char charAddition = toupper(randChar);
		mFullString.push_back(charAddition);
	}
}

void Document::Reinitialize()
{
	auto currChar = mFullString.begin();
	while (currChar != mFullString.end()) {
		int randVal = rand() % 26;
		char randChar = 'a' + randVal;
		char charAddition = toupper(randChar);
		*currChar = charAddition;
		++currChar;
	}
}

std::vector <char>& Document::GetFullString(){
	return mFullString;
}

Document::operator std::string() const
{
	std::string docString;
	for (auto currChar = mFullString.begin(); currChar != mFullString.end(); ++currChar) {
		docString += (*currChar);
	}
	return docString;
}

