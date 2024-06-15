#include "Parser.h"

vector<string> splitString(const string& input, const string& substr)
{
	vector<string> arr;
	
	size_t curr = 0;
	size_t prev = 0;
	while (true)
	{
		 curr = input.find(substr, curr + 1);
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
	string result;	
	string substrNewLine = "\n";
	string substrComment = "//";
	vector<string> splitted = splitString(input, substrNewLine);

	size_t size = splitted.size();
	for(size_t i = 0; i < size; i++)
	{
		size_t curr = -1;
		size_t prev = 0;
		string inputFromSpl = splitted[i];
		while(true)
		{
			curr = inputFromSpl.find(substrComment, curr + 1);
			if (curr == string::npos)
				break;
			inputFromSpl.erase(curr, inputFromSpl.length());
			result += inputFromSpl + "\n";
		}		
	}



	/*while (true)
	{
		curr = input.find(substr, curr + 1);
		if (curr == string::npos)
			break;
		string part = input.substr(prev, curr - prev);
		result += part;
		prev = curr + 1;
	}*/
	return result;
}
