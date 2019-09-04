#include "DocLibrary.h"

DocLibrary::DocLibrary() : mLibrary() {
}

Document* DocLibrary::DequeueFront() {
	Document* frontDoc = mLibrary.front();
	mLibrary.pop_front();
	return frontDoc;
}

void DocLibrary::AddDocument(Document* pDoc){
	pDoc->Reinitialize();
	mLibrary.push_back(pDoc);	
}
