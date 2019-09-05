#include "recent_list.h"


recent_list::recent_list() : mRecents()
{
}



void recent_list::InsertDocument(Document* pDoc)
{
	mRecents.push_back(pDoc);
}
