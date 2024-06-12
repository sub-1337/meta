#pragma once
#include "workingStd.h"

vector<string> splitString(const string& input, const string& str);
string remSubstr(const string& input);

struct ASTLeaf
{
	string value;
	shared_ptr<ASTLeaf> prev;
	shared_ptr<ASTLeaf> next;
};
struct AST
{
	shared_ptr<ASTLeaf> root;
};

class Parser
{
	string textToParse;
public:
	Parser(string text) : textToParse(text)
	{

	};
	virtual ~Parser() = default;
	string RemoveCommentary(string)
	{

	}
	AST Parse()
	{
		AST ast;
		ast.root = make_shared<ASTLeaf>();
		return ast;
	};
};