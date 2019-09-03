#pragma once
#include <array>
#include <vector>

struct Document {
private:
	int mCharCount;
	std::vector <char> mFullString;
	

public:

	Document();

	void Reinitialize();

	std::vector<char>& GetFullString();

	operator std::string() const;
};