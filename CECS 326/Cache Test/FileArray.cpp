#include "FileArray.h"
#include "Document.h"

FileArray::FileArray() 
{
	for (int i = 0; i < mDocumentArray.size(); ++i) {
		mDocumentArray[i] = Document();
	}
}

const Document& FileArray::GetDocAddress(Document& pDocAdr)
{
	auto arrayItr = mDocumentArray.begin();
	auto arrayEnd = mDocumentArray.end();
	while (arrayItr != arrayEnd) {
		if (&(*arrayItr) == &(pDocAdr)) {
			return *arrayItr;
		}
		++arrayItr;
	}
}

const Document& FileArray::GetDocAddress(int pInt)
{
	return mDocumentArray[pInt];
}
