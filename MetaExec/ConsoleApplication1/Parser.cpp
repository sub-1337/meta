#include "Parser.h"

vector<string> splitString(const string& input, const string& str)
{
	vector<string> arr;
	
	size_t curr = 0;
	size_t prev = 0;
	while (true)
	{
		 curr = input.find(str, curr + 1);
		 if (curr == string::npos)
			 break;
		 string part = input.substr(prev, curr - prev);
		 arr.push_back(part);
		 prev = curr + 1;
	}

	string part = input.substr(prev);
	if (part.size() != 0)
		arr.push_back(part);

	return  arr;
}

string remSubstr(const string& input)
{
	return "";
}
