#pragma once
#include <array>
#include "Document.h"
#include <list>
#include <string>

struct recent_list {
private:
	std::list <Document*> mRecents;

public: 
	recent_list();

	bool SearchFor(std::string& docString, std::string& pTerm);

	Document* EjectDocument(Document& pDoc);

	void InsertDocument(Document* pDoc);
};
