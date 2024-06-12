#pragma once
#include "Test.h"
#include "Parser.h"

class TestParser_testOfTests : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		return TestRes(EnumTestRes::ok, "Tests working");
	};
};

class TestParser_misc : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		string code;
		code += "import console;";
		code += "";
		code += "func main()";
		code += "{";
		code += "   print(\"Test\")";
		code += "";
		code += "}";
		Parser parser{"code"};
		AST ast = parser.Parse();
		return TestRes(EnumTestRes::ok, "Misc working");
	};
};

class TestParser_utils_split: public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		vector<string> testOrig = { "a","bb","ccc" };
		vector<string> test = splitString("a;bb;ccc", ";");

		if (std::equal(test.begin(), test.end(), testOrig.begin()))
			return TestRes(EnumTestRes::ok, "splitString");
		else
			return TestRes(EnumTestRes::error, "splitString");
	};
};

class TestParser_utils_split2 : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		vector<string> testOrig = { "a","b","c" };
		vector<string> test = splitString("a;b;c", ";");

		if (std::equal(test.begin(), test.end(), testOrig.begin()))
			return TestRes(EnumTestRes::ok, "splitString");
		else
			return TestRes(EnumTestRes::error, "splitString");
	};
};

class TestParser_utils_split3 : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		vector<string> testOrig = { "a" };
		vector<string> test = splitString("a", ";");

		if (std::equal(test.begin(), test.end(), testOrig.begin()))
			return TestRes(EnumTestRes::ok, "splitString");
		else
			return TestRes(EnumTestRes::error, "splitString");
	};
};


class TestTests : public TestBase
{
public:
	virtual ~TestTests() = default;
	virtual void prepareAll() override		
	{
		addName("Tests");
		addTest(new TestParser_testOfTests());
	}
};

class TestParser : public TestBase
{
public:
	virtual ~TestParser() = default;
	virtual void prepareAll() override
	{
		addName("Parser");
		addTest(new TestParser_utils_split());
		addTest(new TestParser_utils_split2());
		addTest(new TestParser_utils_split3());
		addTest(new TestParser_misc());
	}
};