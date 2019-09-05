#pragma once
#include <array>
#include "Document.h"
#include "recent_list.h"
#include <list>


class FileArray {
private:
	std::array <Document, 36> mDocumentArray;

public:
	FileArray();

	Document* GetDocPointer(Document&);

	Document* GetDocPointer(int);
};