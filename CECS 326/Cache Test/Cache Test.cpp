// Cache Test.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <memory>
#include "Document.h"
#include "FileArray.h"
#include "recent_list.h"
#include "DocLibrary.h"

using namespace std;

//BE SURE TO INCLUDE AN ARRAY OF CHAR VECTOR
int main()
{
	FileArray mainFiles = FileArray();
	cout << "Created Docs" << endl;
	DocLibrary primaryLibrary = DocLibrary();
	cout << "Created Library" << endl;
	recent_list recentList = recent_list();
	cout << "Created Recent List" << endl;
	int i = 0;
	for (i; i < 1024; ++i) {
		primaryLibrary.AddDocument(mainFiles.GetDocPointer(i));
	}
	cout << "Filled Library" << endl;
	for (i; i < 1152; ++i) {
		recentList.InsertDocument(mainFiles.GetDocPointer(i));
	}
	cout << "Filled Recent List";
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
