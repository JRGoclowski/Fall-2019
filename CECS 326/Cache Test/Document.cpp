#include "Document.h"
#include <cstdlib>
#include <string>

Document::Document() : mCharCount(rand() % 1048576 + 2097152), mFullString("")
{
	for (int i = 0; i < mCharCount; ++i) {
		mFullString += 'A' + (rand() % 26);
	}
}

void Document::Reinitialize()
{
	auto currChar = mFullString.begin();
	while (currChar != mFullString.end()) {
		*currChar = 'A' + (rand() % 26);
		++currChar;
	}
}

std::string& Document::GetFullString(){
	return mFullString;
}

