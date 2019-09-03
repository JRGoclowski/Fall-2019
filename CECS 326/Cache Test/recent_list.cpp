#include "recent_list.h"

recent_list::recent_list()
{
	for (int i = 0; i < 128; ++i) {
		auto docAddition = Document();
		mDocumentList.push_back(docAddition);
	}
	for (Document currDoc : mDocumentList) {
		mRecentDocs.push_back(&currDoc);
	}

}

Document* recent_list::SearchFor(std::vector<char> pTerm)
{
	auto termStart = pTerm.begin();
	auto termEnd = pTerm.end();
	for (Document* currDoc : mRecentDocs) {
		auto stringItr = currDoc->GetFullString().begin();
		auto stringEnd = currDoc->GetFullString().end();
		auto termWalker = termStart;
		while (stringItr != stringEnd) {
			if ((*stringItr) == (*termWalker)) {
				termWalker++;
				if (termWalker == termEnd) {
					return currDoc;
				}
			}
			else {
				termWalker = termStart;
			}
			stringItr++;
		}
	}
	return nullptr;
}

Document recent_list::EjectDocument(Document& pDoc)
{
	auto docItr = mDocumentList.begin();
	auto docex = *docItr;
	while (&(*docItr) != &pDoc) {
		docItr++;
		if (docItr == mDocumentList.end()){
			return;
		}

	}
}

void recent_list::InsertDocument(Document& pDoc)
{
	mDocumentList.push_back(pDoc);
	mRecentDocs.push_back(&pDoc);
}
