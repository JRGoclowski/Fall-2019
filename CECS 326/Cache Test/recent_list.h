#pragma once
#include <array>
#include "Document.h"
#include <list>
#include <string>

struct recent_list {


public: 
	recent_list();

	std::list <Document*> mRecents;

	bool SearchFor(std::string& docString, std::string& pTerm);

	Document* EjectDocument(Document& pDoc);

	void InsertDocument(Document* pDoc);
};
