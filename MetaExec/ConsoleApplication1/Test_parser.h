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
			return TestRes(EnumTestRes::ok, "splitString1");
		else
			return TestRes(EnumTestRes::error, "splitString1");
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
			return TestRes(EnumTestRes::ok, "splitString2");
		else
			return TestRes(EnumTestRes::error, "splitString2");
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
			return TestRes(EnumTestRes::ok, "splitString3");
		else
			return TestRes(EnumTestRes::error, "splitString3");
	};
};

class TestParser_utils_remComments2 : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		string orig = "//\n//";

		string output = remComments(orig);

		if (output.find("//") == string::npos)
			return TestRes(EnumTestRes::ok, "remComments2");
		else
			return TestRes(EnumTestRes::error, "remComments2");
	};
};
class TestParser_utils_remComments3 : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		string orig = "";
		orig += "////\n";

		string check = "\n";
		orig += "left // rem\n";
		string output = remComments(orig);

		if ((output.find("//") == string::npos) && (output.find("rem") == string::npos) && (output.find("left") != string::npos))
			return TestRes(EnumTestRes::ok, "remComments3");
		else
			return TestRes(EnumTestRes::error, "remComments3");
	};
};
class TestParser_utils_remComments4 : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		string orig = "";
		orig += "////\n";

		string check = "\n";
		orig += "left // rem\n";

		orig += "left // rem\n";
		string output = remComments(orig);

		if ((output.find("//") == string::npos) && (output.find("rem") == string::npos) && (output.find("left") != string::npos))
			return TestRes(EnumTestRes::ok, "remComments4");
		else
			return TestRes(EnumTestRes::error, "remComments4");
	};
};
class TestParser_utils_remComments_b1 : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		string orig = "";
		orig += "/*";
		orig += "rem";
		orig += "*/\n";
		string output = remComments(orig);

		if ((output.find("/*") == string::npos) && (output.find("rem") == string::npos))
			return TestRes(EnumTestRes::ok, "remComments_b1");
		else
			return TestRes(EnumTestRes::error, "remComments_b1");
	};
};
class TestParser_utils_remComments_b2 : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		string orig = "";
		orig += "/*";
		orig += "rem";
		orig += "*/ left\n";
		string output = remComments(orig);

		if ((output.find("/*") == string::npos) && (output.find("rem") == string::npos) && (output.find("left") != string::npos))
			return TestRes(EnumTestRes::ok, "remComments_b2");
		else
			return TestRes(EnumTestRes::error, "remComments_b2");
	};
};
class TestParser_utils_remComments_b3 : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		string orig = "";
		orig += "/**/";
		orig += "left";
		orig += "/*rem*/\n";
		string output = remComments(orig);

		if ((output.find("/*") == string::npos) && (output.find("*/")) && (output.find("rem") == string::npos) && (output.find("left") != string::npos))
			return TestRes(EnumTestRes::ok, "remComments_b3");
		else
			return TestRes(EnumTestRes::error, "remComments_b3");
	};
};
class TestParser_utils_remComments_b4 : public SingleTestBase
{
public:
	virtual TestRes Run() override
	{
		string orig = "";
		orig += "/*/*rem*/*/ left";
		string output = remComments(orig);

		if ((output.find("rem") == string::npos) && (output.find("left") != string::npos))
		{
			if ((output.find("/*") == string::npos) && (output.find("*/") == string::npos))
				return TestRes(EnumTestRes::ok, "remComments_b4");
			else
				return TestRes(EnumTestRes::warn, "remComments_b4");
		}
		else
			return TestRes(EnumTestRes::error, "remComments_b4");
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
		addTest(new TestParser_utils_remComments2());
		addTest(new TestParser_utils_remComments3());
		addTest(new TestParser_utils_remComments4());
		
		addTest(new TestParser_utils_remComments_b1());
		addTest(new TestParser_utils_remComments_b2());
		addTest(new TestParser_utils_remComments_b3());
		addTest(new TestParser_utils_remComments_b4());
	}
};