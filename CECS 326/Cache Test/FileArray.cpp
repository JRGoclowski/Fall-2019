#include "FileArray.h"
#include "Document.h"
#include <iostream>

FileArray::FileArray() 
{
	for (int i = 0; i < mDocumentArray.size(); ++i) {
		mDocumentArray[i] = Document();
		std::cout << i << std::endl;
	}
}

Document* FileArray::GetDocPointer(Document& pDocAdr)
{
	auto arrayItr = mDocumentArray.begin();
	auto arrayEnd = mDocumentArray.end();
	while (arrayItr != arrayEnd) {
		if (&(*arrayItr) == &(pDocAdr)) {
			return &(*arrayItr);
		}
		++arrayItr;
	}
	return nullptr;
}

Document* FileArray::GetDocPointer(int pInt)
{
	return &mDocumentArray[pInt];
}
