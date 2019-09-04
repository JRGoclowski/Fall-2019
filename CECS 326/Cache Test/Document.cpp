#include "Document.h"
#include <cstdlib>
#include <string>

Document::Document() : mCharCount(rand() % 1048576 + 2097152), mFullString("")
{
	for (int i = 0; i < mCharCount; ++i) {
		char randChar = toupper('a' + (rand() % 26));
		mFullString += randChar;
	}
}

void Document::Reinitialize()
{
	auto currChar = mFullString.begin();
	while (currChar != mFullString.end()) {
		char randChar = toupper('a' + (rand() % 26));
		*currChar = randChar;
		++currChar;
	}
}

std::string& Document::GetFullString(){
	return mFullString;
}

