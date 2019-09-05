#include <iostream>
#include <memory>
#include <vector>
#include <array>
#include <list>

using namespace std;

void Reinitialize(std::string* pString)
{
	auto currChar = pString->begin();
	while (currChar != pString->end()) {
		*currChar = 'A' + (rand() % 26);
		++currChar;
	}
}

bool SearchFor(std::string* docString, std::string& pTerm)
{
	auto stringWalker = docString->find(pTerm);
	if (stringWalker != std::string::npos) {
		return true;
	}
	return false;
}


string* EjectDocument(string* pString, vector<string*> pRecents)
{
	auto docItr = pRecents.begin();
	while (&(*docItr) != &(pString)) {
		docItr++;
	}
	pRecents.erase(docItr);
	return *docItr;
}

int main()
{
	array <string, 1152> mDocuments;
	string stringAddition;
	for (int i = 0; i < mDocuments.size(); ++i) {
		stringAddition = "";
		long stringLength = rand() % 1048576 + 2097152;
		for (int i = 0; i < stringLength; ++i) {
			stringAddition += 'A' + rand() % 26;
		}
		mDocuments[i] = stringAddition;
		cout << i << endl;
	}
	array <string, 15> wordOptions = { "FIRST", "CPP", "REVIEW", "PROGRAM", "ASSIGNMENT",
		"CECS", "BEACH", "ECS", "FALL", "SPRING", "OS", "MAC", "LINUX", "WINDOWS", "LAB" };
	list<string*> primaryLibrary = list<string*>();
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
		for (int i = 1; i < 16; ++i) {
			cout << i << ". " << wordOptions[i] << endl;
		}
		int userInput;
		cout << "Please enter choice, or 16 to exit: ";
		cin >> userInput;
		if (userInput != 16) {
			userInput - 1;
			vector<string*> docsToBeDeleted = vector<string* >();
			for (string* currDoc : recent_list) {
				if (SearchFor(currDoc, wordOptions[i])) {
					docsToBeDeleted.push_back(currDoc);
				}
			}
			auto docWalker = docsToBeDeleted.begin();
			while (docWalker != docsToBeDeleted.end()) {
				primaryLibrary.push_back(EjectDocument(*docWalker, recent_list));
				Reinitialize(*docWalker);
			}
			int docsEjected = docsToBeDeleted.size();
			cout << wordOptions[i] << ": " << docsEjected << "Ejected";
			if (docsEjected != 0) {
				cout << " and reinitialized";
			}
			cout << endl;
			for (int i = 0; i < docsEjected; ++i) {
				auto libFront = primaryLibrary.begin();
				recent_list.push_back(*libFront);
				primaryLibrary.remove(*libFront);
			}
		}
		else
		{
			continueRunning = false;
		}
	}
	cout << "GoodBye!";



}