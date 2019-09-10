#include <iostream>
#include <memory>
#include <vector>
#include <array>
#include <list>
#include <string>

using namespace std;

//Walks through the string, changing each letter
//string* pString - The string to be changed character by character
void Reinitialize(std::string* pString)
{
	auto currChar = pString->begin();
	while (currChar != pString->end()) {
		*currChar = 'A' + (rand() % 26);
		++currChar;
	}
}

//Walks through the string, comparing whenever the walker matches the first letter of the term,
//and then checks if the following characters also match by walking the term walker along with
//the string walker
//string* docString - The string in the document to be searched
//string & pTerm - The term being searched for
// bool - Returns whether or not the doc string contains the term
bool SearchFor(std::string* docString, std::string& pTerm)
{
	auto termStart = pTerm.begin();
	auto termWalker = pTerm.begin();
	auto termEnd = pTerm.end();
	auto stringWalker = docString->begin();
	while (stringWalker != docString->end()) {
		if ((*stringWalker) == (*termWalker)) {
			++termWalker;
			if (termWalker == termEnd) {
				return true;
			}
		}
		else {
			termWalker = termStart;
		}
		++stringWalker;
	}
	return false;
}

//Goes through each document in the recent list until the document to be ejected is found
//Upon finding the document, pushes a pointer to the end of the library, and removes it 
//from the recent list
//string* pString - The string of the document to be ejected
//vector<string*>& pLibrary - the library of files to get from
//vector<string*>& pRecents - the list of recent files to go through
void EjectDocument(string* pString, vector<string*>& pLibrary, vector<string*>& pRecents)
{
	auto docItr = pRecents.begin();
	int count = 0;
	while (*docItr != pString) {
		docItr++;
		count++;
	}
	pLibrary.push_back(*docItr);
	pRecents.erase(docItr);
	return;
}

int main()
{
	array <string, 1152> mDocuments;
	string stringAddition;
	//Instantiate all documents
	for (int i = 0; i < mDocuments.size(); ++i) {
		stringAddition = "";
		long stringLength = rand() % 1048576 + 2097152;
		for (int i = 0; i < stringLength; ++i) {
			stringAddition += 'A' + rand() % 26;
		}
		mDocuments[i] = stringAddition;
		//cout << i << endl;//Debug function
	}

	array <string, 15> wordOptions = { "FIRST", "CPP", "REVIEW", "PROGRAM", "ASSIGNMENT",
		"CECS", "BEACH", "ECS", "FALL", "SPRING", "OS", "MAC", "LINUX", "WINDOWS", "LAB" };

	//Instantiate the library
	vector<string*> primaryLibrary = vector<string*>();
	for (int i = 0; i < 1024; ++i) {
		primaryLibrary.push_back(&mDocuments[i]);
	}

	//Instantiate the recent list
	vector<string*> recent_list = vector <string*>();
	for (int i = 1024; i < mDocuments.size(); ++i) {
		recent_list.push_back(&mDocuments[i]);
	}

	//Primary Function Loop
	bool continueRunning = true;
	while (continueRunning)	{
		//Standard user input prompt
		cout << "Which word would you like to search : " << endl;
		for (int i = 1; i < 16; ++i) {
			cout << i << ". " << wordOptions[(i-1)] << endl;
		}
		int userInput;
		cout << "Please enter choice, or 16 to exit: ";
		cin >> userInput;
		if (userInput != 16) {
			--userInput; //Decrease to have user input match array index
			cout << "Searching for " << wordOptions[userInput] << endl;
			vector<string*> docsToBeDeleted = vector<string* >(); //Keeps track of docs found to not have term
			for (string* currDoc : recent_list) {
				if (SearchFor(currDoc, wordOptions[userInput])) {
					docsToBeDeleted.push_back(currDoc);
				}
			}
			//Walks through recent list and finds each document that does not have the term, and ejects and reinitializes it
			auto docWalker = docsToBeDeleted.begin();
			while (docWalker != docsToBeDeleted.end() && !docsToBeDeleted.empty()) {
				EjectDocument(*docWalker, primaryLibrary, recent_list);
				Reinitialize(*docWalker);
				docWalker++;
			}
			int docsEjected = docsToBeDeleted.size();
			cout << wordOptions[userInput] << ": " << docsEjected << " Ejected";
			if (docsEjected != 0) {
				cout << " and reinitialized";
			}
			cout << endl;
			//Refills the recent list
			for (int i = 0; i < docsEjected; ++i) {
				auto libFront = primaryLibrary.begin();
				recent_list.push_back(*libFront);
				primaryLibrary.erase(libFront);
			}
		}
		else
		{
			continueRunning = false;
		}
	}
	cout << "GoodBye!";



}
