#include <iostream>
#include <memory>
#include <vector>
#include <array>
#include "Document.h"
#include "FileArray.h"
#include "recent_list.h"
#include "DocLibrary.h"

using namespace std;

void Reinitialize(std::string& pString)
{
	auto currChar = pString.begin();
	while (currChar != pString.end()) {
		*currChar = 'A' + (rand() % 26);
		++currChar;
	}
}

int main()
{
	array <string, 1152> mDocuments;
	string stringAddition;
	for (int i = 0; i < mDocuments.size(); ++i) {
		stringAddition = "";
		stringAddition += 'A' + rand()%26;
		mDocuments[i] = stringAddition;
		cout << i << endl;
	}
	array <string, 15> wordOptions = { "FIRST", "CPP", "REVIEW", "PROGRAM", "ASSIGNMENT",
		"CECS", "BEACH", "ECS", "FALL", "SPRING", "OS", "MAC", "LINUX", "WINDOWS", "LAB" };
	vector<string*> primaryLibrary = vector<string*>();
	for (int i = 0; i < 1024; ++i) {
		primaryLibrary.push_back(&mDocuments[i]);
	}
	vector<string*> recent_list = vector <string*>();
	for (int i = 1024; i < mDocuments.size(); ++i) {
		recent_list.push_back(&mDocuments[i]);
	}
	int i = 0;
	bool continueRunning = true;
	while (continueRunning);
	{
		cout << "Which word would you like to search : " << endl;
		for (int i = 0; i < 15; ++i) {
			cout << i << ". " << wordOptions[i] << endl;
		}
		int userInput;
		cout << "Please enter choice, or 16 to exit: ";
		cin >> userInput;
		if (userInput != 16) {
			vector<Document*> docsToBeDeleted = vector<Document* >();
			for (Document* currDoc : recentList.mRecents) {
				if (recentList.SearchFor(currDoc->GetFullString(), wordOptions[i])) {
					docsToBeDeleted.push_back(currDoc);
				}
			}
			auto docWalker = docsToBeDeleted.begin();
			while (docWalker != docsToBeDeleted.end()) {
				primaryLibrary.AddDocument(recentList.EjectDocument(*docWalker));
				(*docWalker)->Reinitialize();
			}
			int docsEjected = docsToBeDeleted.size();
			cout << wordOptions[i] << ": " << docsEjected << "Ejected";
			if (docsEjected != 0) {
				cout << " and reinitialized";
			}
			cout << endl;
			for (int i = 0; i < docsEjected; ++i) {
				recentList.InsertDocument(primaryLibrary.DequeueFront());
			}
		}
		else
		{
			continueRunning = false;
		}
	}
	cout << "GoodBye!";



}