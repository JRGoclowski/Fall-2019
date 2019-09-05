// Cache Test.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <memory>
#include <vector>

#include "Document.h"
#include "FileArray.h"
#include "recent_list.h"
#include "DocLibrary.h"

using namespace std;

//BE SURE TO INCLUDE AN ARRAY OF CHAR VECTOR
int main()
{
	array <string, 15> wordOptions = { "FIRST", "CPP", "REVIEW", "PROGRAM", "ASSIGNMENT",
		"CECS", "BEACH", "ECS", "FALL", "SPRING", "OS", "MAC", "LINUX", "WINDOWS", "LAB" };
	FileArray mainFiles = FileArray();
	cout << "Created Docs" << endl;
	DocLibrary primaryLibrary = DocLibrary();
	cout << "Created Library" << endl;
	recent_list recentList = recent_list();
	cout << "Created Recent List" << endl;
	int i = 0;
	for (i; i < 32; ++i) {
		primaryLibrary.AddDocument(mainFiles.GetDocPointer(i));
		cout << "Added library pointer " << i << endl;
	}
	cout << "Filled Library" << endl;
	for (i; i < 4; ++i) {
		recentList.InsertDocument(mainFiles.GetDocPointer(i));
		cout << "Added recent list pointer " << i << endl;
	}
	cout << "Filled Recent List" << endl;
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
			while (docWalker != docsToBeDeleted.end()){
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

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
