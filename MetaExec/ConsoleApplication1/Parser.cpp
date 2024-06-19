#include "Parser.h"
#include <stack>
#include <utility>
#include <regex>

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

string remComments_line(const string& input)
{
	string result;
	string substrNewLine = "\n";
	string substrComment = "//";
	vector<string> splitted = splitString(input, substrNewLine);

	size_t size = splitted.size();
	for (size_t i = 0; i < size; i++)
	{
		size_t curr = -1;
		size_t prev = 0;
		string inputFromSpl = splitted[i];
		while (true)
		{
			curr = inputFromSpl.find(substrComment, curr + 1);
			if (curr == string::npos)
			{
				result += inputFromSpl + "\n";
				break;
			}
			inputFromSpl.erase(curr, inputFromSpl.length());			
		}
	}

	return result;
}
string remComments_multyLine(string input)
{
	//string result;
	//string startComment = "/*";
	//string endComment = "*/";

	//size_t currStart = 0;
	//size_t currEnd = 0;

	//std::stack<std::pair<string, size_t>> stack;
	//while (true)
	//{
	//	currStart = input.find(startComment, currStart);
	//	if (currStart == string::npos)
	//	{
	//		break;
	//	}			
	//	else
	//	{
	//		stack.push(make_pair(startComment, currStart));
	//	}

	//	currEnd = input.find(endComment, currStart + endComment.length());
	//	if (currEnd == string::npos)
	//	{
	//		break;
	//	}
	//	else
	//	{
	//		if (stack.top().first == "/*")
	//		{
	//			rsize_t prev = stack.top().second;
	//			stack.pop();
	//			if (stack.empty() == true)
	//			{
	//				input.erase(prev, currEnd + endComment.length());
	//			}
	//		}				
	//	}
	//}

	std::regex commentPattern(R"(/\*.*?\*/)");
	return std::regex_replace(input, commentPattern, "");
}
string remComments(const string& input)
{
	string result;	
	result = remComments_line(input);
	result = remComments_multyLine(result);
	return result;
}
