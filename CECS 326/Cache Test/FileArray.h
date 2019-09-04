#pragma once
#include <array>
#include "Document.h"
#include "recent_list.h"
#include <list>


class FileArray {
private:
	std::array <Document, 1152> mDocumentArray;

public:
	FileArray();

	const Document& GetDocAddress(Document&);

	const Document& GetDocAddress(int);
};