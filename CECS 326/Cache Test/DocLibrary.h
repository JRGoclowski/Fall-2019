#pragma once
#include <list>
#include "Document.h"
#include <memory>

class DocLibrary {
private:
	std::list <Document*> mLibrary;

public:

	DocLibrary();

	Document* DequeueFront();

	void AddDocument(Document* pDoc);
};