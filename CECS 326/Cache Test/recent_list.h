#pragma once
#include <array>
#include "Document.h"
#include <list>

struct recent_list {
private:
	std::vector <Document*> mRecentDocs;
	
	std::list <Document> mDocumentList;

public: 
	recent_list();

	Document* SearchFor(std::vector<char> pTerm);

	Document EjectDocument(Document& pDoc);

	void InsertDocument(Document& pDoc);
};
