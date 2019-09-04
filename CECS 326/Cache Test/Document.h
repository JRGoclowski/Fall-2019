#pragma once
#include <array>
#include <vector>
#include <string>

struct Document {
private:
	int mCharCount;
	std::string mFullString;
	

public:

	Document();

	void Reinitialize();

	std::string& GetFullString();
};