#include "recent_list.h"


recent_list::recent_list() : mRecents()
{
}

bool recent_list::SearchFor(std::string& docString, std::string& pTerm)
{
	auto stringWalker = docString.find(pTerm);
	if (stringWalker != std::string::npos) {
		return true;
	}
	return false;
}


Document* recent_list::EjectDocument(Document& pDoc)
{
	auto docItr = mRecents.begin();
	auto docex = *docItr;
	while ((*docItr) != &(pDoc)) {
		docItr++;
	}
	mRecents.remove(*docItr);
	return *docItr;
}

void recent_list::InsertDocument(Document* pDoc)
{
	mRecents.push_back(pDoc);
}
